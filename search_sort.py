import json
import sys
import os
from itertools import islice
import email
import collections



historyFolder = "history"
indexFile = "data/index.json"
rankingFile = "data/ranking.json"


##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]

try :
    sortedResult = []
    
    ##ouvrir l'index
    with open(indexFile) as file :
        index = json.load(file)
        
    ##ouvrir l'index
    with open(rankingFile) as file :
        ranking = json.load(file)

    with open(os.path.join(historyFolder, searchedTerm + ".json")) as file :
        unsortedResult = json.load(file)
        
        sortedResult = []
        i = 0 ;
        for key in sorted(unsortedResult, key=unsortedResult.get, reverse=True):
            sortedResult.append({key : unsortedResult[key]})
            i += 1

        
            
    with open(os.path.join(historyFolder, searchedTerm + ".json"), 'w') as file :
        json.dump(sortedResult, file, indent=4)
            
            
except IOError:
    print("Erreur")

##print(searchedTerm)
