import json
import sys
import os
from itertools import islice


historyFolder = "history"

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]
response = None    

index=0
print(searchedTerm)
##search in history
try :
    with open(os.path.join(historyFolder, searchedTerm)) as file :
        response = json.load(file)
        for key, value in islice(response.iteritems(), 10):
            index+=1
            print(key, value)
            #print("Resultat n° " + index + "\n")
            #print("\tExpediteur : " + resultat["exp"] + "\n")
            #print("\tDestinataire : " + resultat["dest"] + "\n")
            #print("\tSujet : " + resultat["sujet"] + "\n")
            #print("\tMessage : " + resultat["message"] + "\n")
            #print("\Occurences : " + resultat["occurences"] + "\n")
            
            
except :
    print("Erreur")
        
print(response)
