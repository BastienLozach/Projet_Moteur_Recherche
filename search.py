import os
import sys

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]

##Initialisation
##Download, Index, Ranking
os.system(sys.executable + " init.py")

##Historique (et recherche)
os.system(sys.executable + " search_history.py " + searchedTerm)

##Affichage
os.system(sys.executable + " search_show.py " + searchedTerm)

