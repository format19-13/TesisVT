#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
sys.path.append(os.path.abspath(os.pardir))

from configs.settings import *
from data_access.mongo_utils import MongoDBUtils
from requests.exceptions import ChunkedEncodingError
from twython import Twython
from threading import Thread
from Queue import Queue
import streamer_logging
import traceback
import logging
import sys
import time
import pymongo
from pymongo import MongoClient
import imp
from extractUsers import TwitterStreamer
from bio import etiquetarUsuarios
from howold_extractor.scrapingHowold import analyzeProfilePicture
from extractListsSubscriptions import TwitterStreamerSubscriptions

##Mover usuarios etiquetados en paso anterior a la collection "users"
#print "Ejecutando extractUsers.py"
db_access = MongoDBUtils()
db_access.borrarAux()