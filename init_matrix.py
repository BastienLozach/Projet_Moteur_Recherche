import sys
import json
import math

##parametres

##default
inputFile = os.path.join("data", "index.json")
outputFile = os.path.join("data","graphe_chemin.json")
##set
if len(sys.argv) >= 2 :
    inputFile = sys.argv[1]
    if len(sys.argv) >= 3 :
        outputFile = sys.argv[2]

##Debut du script
mailIndex = None

try :
    with open(inputFile, "r") as file :
        
        ##Lecture du fichier
        mailIndex = json.load(file)
        size = 0
        for name, element in mailIndex.items() :
            if element["id"] > size :
                size = element["id"]
        size += 1

        ##initialisation de la matrice
        matrix = []
        for i in range(0,size) :
            line = []
            for i in range(0,size) :
                line.append(0)
            matrix.append(line)
        ##remplissage de la matrice
        for name, data in mailIndex.items() :
            mailId = data["id"]
            mailList = data["dest"]
            ##sum = 0
            for mailSend in mailList :
                k = mailId
                if mailSend in mailIndex :
                    l = mailIndex[mailSend]["id"]
                    matrix[k][l] += 1
                    ##sum += 1
            ##print(k,' : ', name, " :", sum)
            
                
        ##ecriture du fichier
        with open(outputFile, "w") as file :
            file.write(json.dumps(matrix, indent=4))
            
except IOError:
    print("Probleme de lecture")  




