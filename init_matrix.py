import sys
import json
import math

##parametres

##default
inputFile = "data/index.json"
outputFile = "data/graphe_chemin.json"
##set
if len(sys.argv) >= 2 :
    inputFile = sys.argv[1]
    if len(sys.argv) >= 3 :
        outputFile = sys.argv[2]

##Début du script
mailIndex = None

try :
    with open(inputFile, "r") as file :
        
        ##Lecture du fichier
        mailIndex = json.load(file)
        size = len(mailIndex)
        
        ##initialisation de la matrice
        matrix = []
        for i in range(0,size) :
            line = []
            for i in range(0,size) :
                line.append(0)
            matrix.append(line)
          
        ##remplissage de la matrice
        for name, data in mailIndex :
            mailId = data["id"]
            mailList = data["dest"]
            
            for mailSend in mailList :
                i = mailId
                j = mailIndex[maisSend]["id"]
                matrix[i][j] += 1
                
        ##ecriture du fichier
        with open(outputFile, "w") as file :
            file.write(json.dumps(matrix, indent=4))
            
except IOError:
    print("Probleme de lecture")  




