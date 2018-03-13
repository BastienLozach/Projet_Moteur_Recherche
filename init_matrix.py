import sys
import json
import math

##parametres
inputFile = "index.json"
outputFile = "graphe_chemin.json"

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
            mailList = data["send"]
            
            for mailSend in mailList :
                i = mailId
                j = mailIndex[maisSend]["id"]
                matrix[i][j] += 1
                
        ##ecriture du fichier
        with open(outputFile, "w") as file :
            file.write(json.dumps(matrix, indent=4))
            
except IOError:
    print("Probleme de lecture")  




