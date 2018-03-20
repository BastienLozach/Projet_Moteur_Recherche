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
        indexList = json.load(file)
        
    ##ouvrir l'index
    with open(rankingFile) as file :
        rankingList = json.load(file)

    with open(os.path.join(historyFolder, searchedTerm + ".json")) as file :
        unsortedResult = json.load(file)
        
        updatedResult = unsortedResult.copy()
        
        for key, value in updatedResult.items() :
            if (key in indexList):
                expeditor = indexList[key]['id']
                ranking = rankingList[expeditor]
            else :
                ranking = 0.1
            newValue = value + 10 * ranking
            updatedResult[key] = newValue
        sortedResult = []
        i = 0 ;
        for key in sorted(updatedResult, key=updatedResult.get, reverse=True):
            sortedResult.append({key : unsortedResult[key]})
            i += 1

        
            
    with open(os.path.join(historyFolder, searchedTerm + "_sorted" + ".json"), 'w') as file :
        json.dump(sortedResult, file, indent=4)
            
            
except IOError:
    print("Erreur")

##print(searchedTerm)
