##files adresses
mailDirectory = "maildir"
indexFile = "data/index.json"
matrixFile = "data/graphe_chemin.json"
rankingFile = "data/ranking.json"

##initialisation
os.system(sys.executable + " init_download.py")

os.system(sys.executable + " init_index.py " + " " + indexFile + " " + indexFile)

os.system(sys.executable + " init_matrix.py" + " " + indexFile + " " + matrixFile)

os.system(sys.executable + " init_ranking.py" + " " + matrixFile + " " + rankingFile)