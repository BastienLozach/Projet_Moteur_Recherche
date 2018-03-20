import sys
import json
import math

##parametres

##default
inputFile = "data/graphe_chemin.json"
outputFile = "data/ranking.json"

##set
if len(sys.argv) >= 2 :
    inputFile = sys.argv[1]
    if len(sys.argv) >= 3 :
        outputFile = sys.argv[2]

##Fonction
def multiplyMatrixByVector(matrix, vector) :
    result = []
    size = len(vector)
    for i in range(0, size) :
        value = 0;
        for j in range(0, len(matrix)) :
            value = math.fsum([value, vector[j] * matrix[j][i]])
        result.append(value)
    return result

##Debut du script
linkMatrice = None

try :
    with open(inputFile, "r") as file :
        ##Lecture du fichier
        linkMatrice = json.load(file)
        
        ##Normalisation de la Matrice
        normalisedMatrice = []
        for line in linkMatrice :
        
            total = sum(line)
            if total != 0 :
                new_line = [float(i/total) for i in line]
            else :
                new_line = [0 for i in line]
            normalisedMatrice.append(new_line)
        
        ##Ranking
        size = len(normalisedMatrice[0])
        if size != 0 :
            vector = []
            vector2 = []
            for i in range(0, size) :
                vector2.append(1/size)
            iteration = 0
            while vector != vector2 and iteration < 50:
                temp = vector2
                vectorTemp = multiplyMatrixByVector(normalisedMatrice, vector2)
                vector2 = []
                total = 0
                for i in vectorTemp :
                    total += i
                vector2 = [float(i)/total for i in vectorTemp ]
                vector = temp
                iteration += 1
                
            ##arrondi
            for i in range(0, len(vector2)) :
                value = format(vector2[i], '.4f')    
                vector2[i] = value
                
            ##ecriture du fichier
            with open(outputFile, "w") as file :
                file.write(json.dumps(vector2, indent=4))
except IOError:
    print("Probleme de lecture")  




