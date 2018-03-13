import sys
import re
from six.moves.urllib.request import urlopen
import json
import math

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

##Début du script
inputFile = "graphe_chemin.json"
linkMatrice = None
try :
    with open(inputFile, "r") as file :
        linkMatrice = json.load(file)
        print("test")
except IOError:
    print("Probleme de lecture")  

normalisedMatrice = []
for line in linkMatrice :
    
    total = sum(line)
    if total != 0 :
        new_line = [float(i/total) for i in line]
    else :
        new_line = [0 for i in line]
    normalisedMatrice.append(new_line)


print(normalisedMatrice)
size = len(normalisedMatrice[0])
if size != 0 :
    vector = []
    vector2 = []
    for i in range(0, size) :
        # vector.append(1/size)
        vector2.append(1/size)
    print(vector2)
    iteration = 0
    while vector != vector2 and iteration < 50:
        temp = vector2
        vectorTemp = multiplyMatrixByVector(normalisedMatrice, vector2)
        vector2 = []
        #normalisation
        total = 0
        for i in vectorTemp :

            total += i
        vector2 = [float(i)/total for i in vectorTemp ]
        #normalisation

        print(vector2)
        vector = temp
        iteration += 1
        #print("v == v :", vector != vector2)
        #print("iteration :", iteration)
    sum = 0
    for i in vector2 :
        sum += i
    print(sum)
    
    ##arrondi
    for i in range(0, len(vector2)) :
        value = format(vector2[i], '.4f')    
        vector2[i] = value
    with open("Boye_Lozach_MR_TP4_Resultat_Ranking.json", "w") as file :
        file.write(json.dumps(vector2, indent=4))

print("-------------------------------")
print('Vecteur Trouvé')
        
print("-------------------------------")
print('fini !')


