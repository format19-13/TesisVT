import os,sys
import os.path

sys.path.append(os.path.abspath(os.pardir))

from enum import Enum

DIR_PREFIX="/Users/verouy" #MAC
#DIR_PREFIX="/home/vero" #LINUX

############################
# LOGGER
############################
LOGGING_BASE_PATH = '/var/log/twitter_streamer/'
LOGGING_ROOT_NAME = 'logfile'

############################

############################
# STREAMER
############################
TWITTER_ACCESS_KEYS = {
    "app_key": "U20LyEZpsROJSo1hE3GdSigC6",
    "app_secret": "u75pnyuv6nBvsdTpeC75j7OdXobgNqRoZekPyP8l8GlYYO6Rfm",
    "app_access_token": "780859625448939521-XZ0Pz1XH4fXBQuTZwYjoL49fTLMQSbK",
    "app_access_token_secret": "fiWErePI0a0KiKlwMvu9VRXXYN7ZdrAmFMiGhFouHsAWE",
    "description": "Twitter access key"
}

TRACK_TERMS = ''

# Cuentas a escuchar: Lista de IDs de cuentas de Twitter en un string separado por comas
FOLLOWS_IDS =''

# Montevideo
BOUNDING_BOXES = [-56.96411, -35.09295,-53.53638, -33.68778]
#-71.54296875,-52.8558641779 -66.005859375,-23.926013033 -53.4375,-32.9533681458 -71.54296875,-52.8558641779]
#                    -56.96411, -35.09295,
#                   -53.53638, -33.68778


############################

PLACES_COUNTRY_IDS = ['UY']

# EXTRACTOR
CANT_WORKERS = 2


class EnumSource(Enum):
    GEOLOCATION = "geolocation"
    TRACKTERMS = "trackterms"
    FOLLOW = "follow"

SOURCE = [EnumSource.GEOLOCATION, EnumSource.TRACKTERMS, EnumSource.FOLLOW]


class EnumSource(Enum):
    SCREEN_NAMES = "screen_names"

SOURCE = [EnumSource.SCREEN_NAMES]
#SCREEN_NAMES="ralphalmuser,pachogruas,mrtfernandez,rrebolledo,maria_vega_,gemaconga,olgarodriguezfr,vigelacoaching,alvarogarciap90,mmendizabal1,naturalvoyager,beltran_lola,h_torres,isanseba,ncampos,mistrals,manushgalvan,mfeijoo,juancarcubeiro,a_valenzuela,srouvier,antoniorull,abarceloh25,juanma_nieves,alberto_blanco,alexandraaberr,ser_seo,gomezdelpozuelo,angelmgtech,marta_dominguez,maripuchi,jsanchezfranco,adela_micha,sboxcoaching,naruedyoh,anablanco_tve,rhmedia_es,juantorreslopez,garciaaller,maritriniginer,mabelbullon,jmgomezperez,luistomala,chgarciacortes,javierbri,sorianomarina,ojecua,jesusferre,shora,helenaancos,claudiogarcia82,cati_nicolau,maitefinch,rafadiaz1,marielabejar,carlosecue,oscargcervella,nagodelos,segundaopor,hawbi,emiliodebenito,realqueenpink,emoragues,espinosa_albert,ginesalarcon,mmmendieta,mar_malabo,perezreverte,felixbernet,moveiter,cesardalmau,mateodomenech,prodigy_man,yvonic55,fjaureguic,vanis,diegoisabel1,mikomonik,mariupaolini,josetrecet,silviacobo,thffernando,pfcdgayo,titatorro,helenaresano,hectormilla,jgarridoo,biogeocarlos,sandra_garciaf,pep_jimenez,joancmarch,heteronima,etnika,sebasmuriel,lopezdoriga, diegocobelo,globalbrand_,pabloformoso,ivanpuente,quiquemateuvlc,julietabolullo,mrgomezponce,jesusencinar,jordimirobruix,robcarballo,pepecuesta,carmechaparro,juancmselma,juliagomezcora,morenobarber,yoleidycarvajal,monicamoro,mranera,soozmoody,juanant_galindo,evacolladoduran,laciencibilidad,copano,jalguerrero,nuriarocagranel,alfonsomarco,david_carnicer,elenhitaes,lutxana,carmen_rrhh,pilarroch,globaltattooma,ohcarool,ovibarcelo,acedotor,kicorangel,cesarpiqueras,jgonzalez_es,rosamariaartal,ebdtraining,ramirofortea,galachitaa,petezin,worldreaders,susannagriso,salvarbi, elenavama,clementealvarez,luvsayal,albertoartero,cesarfitness,joanplanas,victoriabioque,milaximenez,webempresa20,hector_cabrera_,anamariallopis,jesusgallent,fernand0,nataliagomez_es,virgula,lourdesmunoz,leonardpera,kenshin23,pilarajev,corallarrosa,ytzvan,rozyo_,energica,juanmerodio,almarro1,granero,mgdelpozuelo,catyforteza,miss_belmont,aliciapomares,chapoypati,acoronadoc,andreurobuste,carlosbecler,anavidalegea,msconcu,gabiplanas_rrhh,billiesastre,arangocoaching,pcvillarcayo,diegolleo,cris_villanueva,belenboville,javiersalinas00,carlosguadian,sergeyodintsov,tereamor,eblanperis,lourdesverger,factoriagris,respetocanas,charoizquierdo,perejoanmitjans,carolinagavilan,_anamilan_,wellcomm,rodriguezbraun,gomezrufo,albeitar,manuelgimnez,elissambura,el_pakozoico,luisdiazdeldedo,mlaudisio,luisgosalbez,acliment,etcomusic,esperanzaguirre,e_valero,cutefilm,cdelamortve,flowergirona,carmengelices,pablo_astudillo,sarabarass,crisalonsofran,auroraferrer,pedrobiurrun,alesonline,juanlusanchez,seeseuno,lourdesmoralesg,miguel_a_alonso,ejoana,monicadeza,juancbarcelo,adelaidauma,vdgracia,teresa_perales,hacheromero,juanjomorodo,luismiguelcas,jogartra,ingeosolum,amigerpe,tinofernandez,bibiladi,iescolar,socialsmr,csaavedrasexta,carmenalcayde,elviralindo,martarodrigueza,,eapesteguia,luislopezcuenca"
#STREAMER RETURNS ERROR FOR THESE USERS: pauroda,croibal,jdelagrana,reygarrido
#USERS NO LONGER ACTIVE="cati_nicolau,csaavedrasexta,etcomusic,hawbi,laciencibilidad,mar_malabo,realqueenpink, rozyo_, salvarbi, sarabarass, seeseuno, socialsmr, yvonic55"
#TOTAL USERS IN DB: 233 (might be needed to run again extractUsers to add "ohcarool")
SCREEN_NAMES="chrisguevarauy,marubrici,brunopintom,roomiflores_,juanmusumeci07,tamaracolmaan,roburato1,mlpassio,vanemtl,ampii_sola,andradaceleste,anttomartina,dianamateos10,natalia62936723,nachogmoreira,julidorado15,florburelli,lucrerusa2,michael_sorano,daaaibravo5,giulianodanok,roohernande,inmonoel,juliett1215,natiferreirac,_brisa17abigail,luusimonini,sofi_devega,zoyasanchez,agustinavilch17,ro_castiglioni,celeste0234,mili_campos_,agus_gonzalez26,vicky_larrosa1,carolina__01,nikysemeria,roominalucia,faculiencres,lucasilva016,vanes3996,rubiaaaenana,natanahelcndf,12arielsosa,elianamartin8,marcecosta1891,vale9850,institutoui,carlos___g,rosariomagnou,candelarodrgu13,carburandotv,fedeabatangelo,alejandroide_25,brian_matassa,alemandra19,mmarcosgodoy97,liilu_franco,aguuus28,yanella_salatto,tomii0410,jhohanaaaam,clauditah_nn,lucia_villar,jennbardecio,valentinaaa1297,biosistemasuy,lulypeteanc,francocairo02,jul14nbarissani,pamemememesia15,gabrielf0rmento,facuufrancese5,mikaag_smile,enzosantander14,camfla,marsitavidal,leogomez9999,015edith,brianinsuacjs,fransaxlund,bettiaguilera,nicouuss,oriigartland,bekernanni,joakomirasol,solemi245,maurivilaa,nahir_intorre,fraancodaaniel1,jurimarok,zanoni_f,francoserra17,facumeneses,paulapinzone,valentinademarc,rociovecino_18,federiicogrosso,paulacorrea_11,neverlandlss,miqaela_dagna,juiglesias07,sebatorok,damianloyarte,julianaorellano,facusuarez08,carlosgomezuy,brianramirez98,silvakaren8,cbdk2011,micaelaagomeez1,anitafraga,revistahipismo,lucianovillalv1,astrosgarbuyo,yanymombelli04,camilasayus,maguicamposs,damindylanpino1,manu_zarzoso,alerojas1995,majo_floress,antoscodellaro,yulijusto13,yamilafajar,roomiicaceress,milibarrio_,victoriacarrat2,kareenhubscher,patitolujan75,rtafernaberry,cascarilla3,belicornio1998,diaznap,ezequielherraiz,djnilogb,antogabas,toni_pre,meliijiji,milii1224,plakards,dorregocaro,pablopiriz17,elvikingogordo,yuliireynoso,karusilva1,lucasanhornok,paufrancisco123,chicabostera1,criscedola,caritofrias99,mateofagundez,camiacosta1891,lautaurtiaga,micaela59134889,sanabria_daiana,rossanaduarte1,camila_martino,nataliamindurry,nadiaohaco,terevazquez_12,littlepearlblue,nachielhh,laurabat55,el_huno,nico_lopez0,camiib14,luzcattaneo,maarupicerno,coty_gastaldo,joyfernandz,andresaf170198,jhonagarcia5,selenebasualdo,lucilagav,luzdaiiana,flocamarano,estefiperezok,nikko_cabrera,gonzalopessano_,dangaer,cccccccaro,sofiintvg,faccumu,gonzamederos1,agusmerlojr,mariouberti,projaok,karolse48822803,daiogarcia2,oliverapipi,leytonley,cgezzio,fraacoronel,galebuena,melo_snowflake,ssdiaz19,camilaceleste96,santirayu,aguusdell_, briangonzaa,diegocastagno,castillofran20,laligoias,vicoelgart,jessicapr1202,nellygalotta,alvaropereyraa,marcelo_pedrozo,galonsobenia,santiagopepe_91,puchoacuarp,cuervolobos,pedro_guzmant,stagno_chiara,ellniiicoo,caraballoce,ivandjdv,melisafreiria,pizzasingkaraok,candelamachado7,geral_centu,lopeznic4,byimpactada,belugolfarini,fioventura,ani_0697,juaniruss,duartenahuee,fbreganti,ludfdz102,lapipydeltricoo,mikaela241206,antoorsetti_,rodrigueeez666,jb_joacobolso,julianrosa00,joseplut104,circuitoc56,anahirrii,grupohasar,gabyscarpato,matyasnicolas98,antotusa,nacho744,nahuelrussialv1,nahucatuok,martinfagundez,delfibruzzone,andreamachado57,bengochea_sb,cocomendeguia54,santiberto8,natinv30,norberto1956,federicamarilla,genegutierrez3,miligimenezntvg,maxiifalconnat,g6d2p,_sofi_41,bica199,facuureynoso99,lnahuelfb,blasesquenon,catii_menna,28bernardita,abrucelibertiok,publicisimpetu,josemramirez26,neri_oriana,sebbasok,pas_de_bourre,dosalmasunamor,maru_cabj21,candepalacios1,mirtha4620,iaann_1999,floridatele,velazquezkevin1,mauriciozarauz,agusvidall2,felipepaullier,rojasmimi,per_reynoso,floorcei,aldanacumler,cabj_ayrton,romigaray2,camionrrubio,fabianparcerito,valelucas_95,tatianamartin3z,arandagustina,axelfansmfet,valeacevedo98,marcosfontaine7,paulimoraless,vcastroemilia,jorge_frias1968,el_patoherrera,elritual,barrsosa35,facubringa,hectorcanedo2,roldanrodrigo3,jluisfoglia,ruthy_yucra,nicolastripoli,rosoimuro,sugacabrera,tamitoledovazq,lucianocabj110,jeffpaternalok,zooerivas77,demarcobianca,alexistokayukok,annto_b,mmusitani,matiasnicolet,ortizmarcos18,jorvilares,facundodelpuer2,luucasnico,agusfiguere,nicolasmesa93,juanialtezor,valenvelez95,jazdistefaano,spastrana_01,sistimartin,daniimndez1,belenmansur,milulaarroquy,luuli_espeche15,fran_sacco,lariramirez4,juampps,abybeautyexpert,javyyvarela,iaanerik,santiimontielok,bautiperezz1899,caciquepaiva09,carboneraa1891,pampifc,gustavoanselmi1,gfran93,locambie,orellanojuliana,braiant93432642,rominadaniela09,lu_leg_,lajoya14,anarivas_35,liberluna,mapriconfcalsa,cayuyulii,jennyabigail7,amapolaa21,brmvcc,luzzcoficial1,robertdelcap,nahubacigaluppi,joseerosaa,alan_corrarello,ludtaborda"
#no andan: carrettonilucho,thiagobarriosrp,peralta_sofiia,aguram1,amapolaa21
#429 x ahora