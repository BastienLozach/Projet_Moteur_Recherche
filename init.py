import os
import sys

##files adresses
mailDirectory = "maildir"
indexFile = os.path.join("data", "index.json")
indexDir = "index"
matrixFile = os.path.join("data", "graphe_chemin.json")
rankingFile = os.path.join("data", "ranking.json")

##creation du dossier data
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("history"):
    os.makedirs("history")

##initialisation
##telechargement
if not os.path.exists(mailDirectory):
    os.system(sys.executable + " init_download.py")    

##indexage des expediteurs
if not os.path.exists(indexFile):
    os.system(sys.executable + " init_index.py " + " " + mailDirectory + " " + indexFile)       

##indexage des mails
if not os.path.exists(indexDir):
    os.system(sys.executable + " init_index_mails.py")       


##matrice
if not os.path.exists(matrixFile):
    os.system(sys.executable + " init_matrix.py" + " " + indexFile + " " + matrixFile)

##ranking
if not os.path.exists(rankingFile):
    os.system(sys.executable + " init_ranking.py" + " " + matrixFile + " " + rankingFile)
