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

##Search
os.system(sys.executable + " search_history.py " + searchedTerm)

