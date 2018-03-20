import json
import sys
import os
from itertools import islice
import email


historyFolder = "history"

##parametres

##default
searchedTerm = "box"
##set
if len(sys.argv) >= 2 :
    searchedTerm = sys.argv[1]

print(searchedTerm)
