import json

inputPageRank = "Boye_Lozach_MR_TP4_Resultat_Ranking.json"
inputCloseness = "Boye_Lozach_MoteurRecherche_TP4_Resultat_Closeness.json"
output = "Boye_Lozach_MoteurRecherche_TP4_Resultat.json"
outputcsv = "Boye_Lozach_MoteurRecherche_TP4_Resultat.csv"

pageRank = None
closeness = None

try :
    with open(inputPageRank, "r") as file :
        pageRank = json.load(file)
except IOError:
    print("Probleme de lecture")
    
try :
    with open(inputCloseness, "r") as file :
        closeness = json.load(file)
except IOError:
    print("Probleme de lecture")

result = []    
for i in range(0,len(pageRank)) :
    value = {
        "id" : i,
        "pageRank" : pageRank[i],
        "closeness" : closeness[i] 
    }
    result.append(value)

try :
    with open(output, "w") as file :
        json.dump(result, file, indent=4)
except IOError:
    print("Probleme d'écriture")
    
try :
    with open(outputcsv, "w") as file :
        for line in result :
            file.write(str(line["pageRank"])+";"+str(line["closeness"])+"\n")
except IOError:
    print("Probleme d'écriture")