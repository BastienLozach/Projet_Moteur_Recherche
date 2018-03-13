import os
import sys

##files adresses
mailDirectory = "maildir"
indexFile = "data/index.json"
matrixFile = "data/graphe_chemin.json"
rankingFile = "data/ranking.json"

##creation du dossier
directory = os.path.dirname(mailDirectory)
if not os.path.exists(directory):
    os.makedirs(directory)

##initialisation
#os.system(sys.executable + " init_download.py")

os.system(sys.executable + " init_index.py " + " " + mailDirectory + " " + indexFile)

os.system(sys.executable + " init_matrix.py" + " " + indexFile + " " + matrixFile)

os.system(sys.executable + " init_ranking.py" + " " + matrixFile + " " + rankingFile)