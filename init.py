import os
import sys

##files adresses
mailDirectory = "maildir"
indexFile = "data/index.json"
matrixFile = "data/graphe_chemin.json"
rankingFile = "data/ranking.json"

##creation du dossier data
if not os.path.exists("data"):
    os.makedirs("data")

##initialisation
##telechargement
if not os.path.exists(mailDirectory):
    os.system(sys.executable + " init_download.py")    

##indexage
if not os.path.exists(indexFile):
    os.system(sys.executable + " init_index.py " + " " + mailDirectory + " " + indexFile)       

##matrice
if not os.path.exists(matrixFile):
    os.system(sys.executable + " init_matrix.py" + " " + indexFile + " " + matrixFile)

##ranking
if not os.path.exists(rankingFile):
    os.system(sys.executable + " init_ranking.py" + " " + matrixFile + " " + rankingFile)