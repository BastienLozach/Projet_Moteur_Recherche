import json
import sys
import os
from itertools import islice
import email


historyFolder = "history"

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]
response = None    

index=0
print("Mot Recherché : ", searchedTerm)
##search in history
try :
    with open(os.path.join(historyFolder, searchedTerm + ".json")) as file :
        response = json.load(file)
        for line in islice(response, 10):
            mailFileName = list(line.keys())[0]
            nbOccurences = line[mailFileName] 
            index+=1
            msg = email.message_from_file(open(mailFileName))
            print("Resultat n° " + str(index) + "\n")
            print("\tFichier : " + mailFileName)
            if msg['From']:
                print("\tExpediteur : " + msg["From"])
            if msg['To']:
                destList = msg["To"].split(",")
                print("\tDestinataire " + ("(Total " + str(len(destList)) + ")" if len(destList) > 10 else "" ) +": " + ",".join(islice(destList, 10)) + ( ", ..." if len(destList) > 10 else "" ))
            if msg['Subject']:
                print("\tSujet : " + msg["Subject"])
            print("\tOccurences : " ,nbOccurences, "\n")
            
            
except IOError:
    print("Erreur")
        
#print(response)
