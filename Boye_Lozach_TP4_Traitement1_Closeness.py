import json
##Lire le json
inputFile = "graphe_chemin.json"
distanceFile = "distance.json"
outputFile = "Boye_Lozach_MoteurRecherche_TP4_Resultat.txt"
outputFileJson = "Boye_Lozach_MoteurRecherche_TP4_Resultat_Closeness.json"

matrix = None ;
try :
    with open(inputFile, "r") as file :
        matrix = json.load(file)
except IOError:
    print("Impossible de lire le fichier")  
size = len(matrix)
maxK = int(size/12)
##distance : algorithme de Floyd Warshall
def distance(i, j, k=maxK) :
    print("distance :\t", str(i), "\t", str(j), "\t", str(k))
    if i == j :
        return 0
    if k == 0 :
        if matrix[i][j] == 1 :
            return 1
        else :
            return 10000
    else :
        return min(distance(i, j, k-1), (distance(i, k-1, k-1) + distance(k-1, j, k-1)) )

##calcul de distance !
distanceMatrix = []
for i in range(0, size) :
    distanceMatrix.append([])
    for j in range(0, size) :
        distanceMatrix[i].append(distance(i, j))

try :
    with open(distanceFile, "w") as file :
        json.dump(distanceMatrix, file, indent=4)
except IOError:
    print("Probleme d'ecriture")  


##Closeness centrality

result = []
for i in range(0, size):
    denominateur = 0 ;
    for j in range(0, size) :
        denominateur += distanceMatrix[i][j]
    indice = (size-1)/denominateur ;
    result.append(indice)
    
#try :
    #with open(outputFile, "w") as file :
        #for i in range(0, len(result)) :
            #file.write(str(i) + "\t" + str(result[i])+"\n") 
#except IOError:
    #print("Probleme d'ecriture")
    
try :
    with open(outputFileJson, "w") as file :
        json.dump(result, file, indent=4)
except IOError:
    print("Probleme d'ecriture")  