import json
import sys
import os


historyFolder = "history"

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]
response = None    
##search in history
try :
    with open(os.path.join(historyFolder, searchedTerm + ".json")) as file :
        response = json.load(file)
except :
    os.system(sys.executable + " search_function.py " + searchedTerm)
    os.system(sys.executable + " search_sort.py " + searchedTerm)
    
    ##second try
    try :
        with open(os.path.join(historyFolder, searchedTerm + ".json")) as file :
            response = json.load(file)
    except :
        a = "Do nothing"

##pour forcer un second tri
os.system(sys.executable + " search_sort.py " + searchedTerm)