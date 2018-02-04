
import os,sys
import os.path
import numpy as np
import pandas as pd
sys.path.append(os.path.abspath(os.pardir))
from sklearn.model_selection import train_test_split
from configs.settings import *
from data_access.mongo_utils import MongoDBUtils
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import itertools
import time
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score

def main_customFields(typeOp):

	## *********ARMO EL DATASET DE TRAIN Y EL DE TEST *********
	db_access = MongoDBUtils()
	users_df = db_access.get_customFields(typeOp)

	# Split into training and test set
	# 80% of the input for training and 20% for testing

	train_data=users_df.sample(frac=0.8,random_state=200) 
	test_data=users_df.drop(train_data.index)

	# Show the number of observations for the test and training dataframes
	print 'Number of observations in the training data:', len(train_data)
	print 'Number of observations in the test data:',len(test_data)
		
	# Create a list of the feature column's names (everything but the screen_name and age)
	features = users_df.columns[1:(len(users_df.columns)-1)]

	import ml_utils as ml_utils

	# convert age ranges into integers
	y = ml_utils.convertToInt(train_data['age'],typeOp)

	# Create a random forest Classifier.
	rforest = RandomForestClassifier(n_jobs=2, random_state=0)
	
	# Initialize Multinomial Naive Bayes
	bayes = MultinomialNB()

	svm = LinearSVC(loss='hinge', penalty='l2', random_state=42)
	
	sgd = SGDClassifier(loss='hinge', penalty='l2', random_state=42, alpha=0.001)

	# Train the Classifier to take the training features and learn how they relate to the age
	rforest.fit(train_data[features], y)

	bayes.fit( train_data[features], y ) 
	
	svm = svm.fit(train_data[features], y) 
	
	sgd= sgd.fit(train_data[features], y ) 
	
	# Apply the Classifier we trained to the test data
	# Create actual english names for the ages for each predicted age range
	resultForest = ml_utils.convertToCategory(rforest.predict(test_data[features]),typeOp)
	resultBayes = ml_utils.convertToCategory(bayes.predict(test_data[features]),typeOp)
	
	resultSVM= ml_utils.convertToCategory(svm.predict(test_data[features]),typeOp)

	resultSGD= ml_utils.convertToCategory(sgd.predict(test_data[features]),typeOp)

	# View the predicted probabilities of the first 10 observations
	rforest.predict_proba(test_data[features])[0:10]

	#############################################
	# EVALUATE THE MODEL
	#############################################

	outdir =time.strftime("%d-%m-%Y")
	
	if not os.path.exists(outdir):
   		os.mkdir(outdir)

   	if not os.path.exists(outdir +"/"+typeOp):
   		os.mkdir(outdir +"/"+typeOp)

   	outdir=outdir +"/"+typeOp

   	ageRanges=[]
   	if typeOp=='normal':
   		ageRanges=db_access.getAgeRanges()
   	else:
   		ageRanges=db_access.get3AgeRanges()

	##RANDOM FOREST
	ml_utils.createConfusionMatrix(test_data['age'].tolist(),resultForest,ageRanges,'customFields','RandomForest',outdir)
	
	##BAYES
	ml_utils.createConfusionMatrix(test_data['age'].tolist(),resultBayes,ageRanges,'customFields','NaiveBayes',outdir)
	
	##SVM
	ml_utils.createConfusionMatrix(test_data['age'].tolist(),resultSVM,ageRanges,'customFields','SVM',outdir)
	
	##SGD
	ml_utils.createConfusionMatrix(test_data['age'].tolist(),resultSGD,ageRanges,'customFields','SGD',outdir)
	
	# View a list of the features and their importance scores
	print "Importance of Features: ", list(zip(train_data[features], rforest.feature_importances_))

	# Copy the results to a pandas dataframe 
	output = pd.DataFrame( data={"id":test_data["screen_name"], "realAge":test_data["age"], "ageRandomForest":resultForest,"ageNaiveBayes":resultBayes})
	#print output

	outname = 'ml_customFields_result.csv'
	fullname = os.path.join(outdir, outname)    
	output.to_csv(fullname,index=False)

	accuracyRF = accuracy_score(test_data['age'].tolist(), resultForest)
	accuracyNB = accuracy_score(test_data['age'].tolist(), resultBayes)
	accuracySVM = accuracy_score(test_data['age'].tolist(), resultSVM)
	accuracySGD = accuracy_score(test_data['age'].tolist(), resultSGD)

	fscoreRF = f1_score(test_data['age'].tolist(), resultForest, average=None, labels=ageRanges)
	fscoreNB = f1_score(test_data['age'].tolist(), resultBayes, average=None, labels=ageRanges)
	fscoreSVM = f1_score(test_data['age'].tolist(), resultSVM, average=None, labels=ageRanges)
	fscoreSGD = f1_score(test_data['age'].tolist(), resultSGD, average=None, labels=ageRanges)

	print "ACCURACY--> Bayes:",accuracyNB,"|RForest:", accuracyRF,"|SVM:", accuracySVM,"|SGD:", accuracySGD
	print "F-SCORE--> Bayes:",fscoreNB,"|RForest:", fscoreRF,"|SVM:", fscoreSVM,"|SGD:", fscoreSGD
	
	return "ACCURACY--> Bayes:",accuracyNB,"|RForest:", accuracyRF,"|SVM:", accuracySVM,"|SGD:", accuracySGD,"F-SCORE--> Bayes:",fscoreNB,"|RForest:", fscoreRF,"|SVM:", fscoreSVM,"|SGD:", fscoreSGD

if __name__ == '__main__':
    main_customFields()

    #https://chrisalbon.com/machine-learning/random_forest_classifier_example_scikit.html
    #http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
