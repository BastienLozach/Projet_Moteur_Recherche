import json

inputFile = "rollernet.dyn"
outputFile_weighted = "graphe_pondere.json"
outputFile_binary =  "graphe_chemin.json"

##entre 20 et 30 minute
start = 15*60 ;
end = 45*60 ;

weightedMatrix = []
binaryMatrix = []
for i in range(0,62) :
    weightedMatrix.append([])
    binaryMatrix.append([])
    for j in range(0,62) :
        weightedMatrix[i].append(0)
        binaryMatrix[i].append(0)
        
try :
    with open(inputFile, "r") as file :
        ##lire toutes les lignes
        for line in file :
            line = line.strip()
            array = line.split(" ");
            if start <= int(array[2]) < end :
                #sens 1
                weightedMatrix[int(array[0])][int(array[1])] += 1
                binaryMatrix[int(array[0])][int(array[1])] = 1
                #reciproque
                weightedMatrix[int(array[1])][int(array[0])] += 1
                binaryMatrix[int(array[1])][int(array[0])] = 1                
except IOError:
    print("pas de fichier")

try :
    with open(outputFile_weighted, "w") as file :
        json.dump(weightedMatrix, file, indent=4)
except IOError:
    print("Probleme d'ecriture")
    
try :
    with open(outputFile_binary, "w") as file :
        json.dump(binaryMatrix, file, indent=4)
except IOError:
    print("Probleme d'ecriture")    