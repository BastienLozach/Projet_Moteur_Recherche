import email
import os
import json
import sys

historyFolder = "history"
inputFile = "maildir"

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]

def get_search(motRecherche):
    res = {}
    le_dossier = 0
    le_sous_dossier = 0
    i = 1
    listeDesMails = []
    occurence = {}
    total = 1               
    for folder, subs, files in os.walk(inputFile):
        for mailFile in files:
            try :
                cibleMail = os.path.join(folder, mailFile)
                mail = open(cibleMail).read()
                b = email.message_from_string(mail).get_payload()
                msg = email.message_from_file(open(cibleMail))
                if msg['Subject']:
                    Subject = msg['Subject']
                    b = Subject + " " + b
                nombreDeFois = b.count(motRecherche)
                if nombreDeFois != 0:             
                    occurence[cibleMail] = nombreDeFois
                print("\rPas de crash ! mail : " + str(total), end="") 
                total += 1
            except Exception :
                a = "do nothing"
    
                   
    return occurence

commande = get_search(searchedTerm)

##ecriture du fichier
with open(os.path.join(historyFolder, searchedTerm + ".json"), "w") as file :
    json.dump(commande, file, indent=4)
