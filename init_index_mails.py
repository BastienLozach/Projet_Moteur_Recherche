import email
import os
import collections
import json
import re

inputFile = "maildir"
outputFile4 = os.path.join("index","less_than_four_letters")
outputFile4or5 = os.path.join("index","four_or_five_letters")
outputFile5 = os.path.join("index","more_than_five_letters")

if not os.path.exists("index"):
    os.makedirs("index")

if not os.path.exists(outputFile4):
    os.makedirs(outputFile4)

if not os.path.exists(outputFile4or5):
    os.makedirs(outputFile4or5)

if not os.path.exists(outputFile5):
    os.makedirs(outputFile5)

def index_four_or_five_letters_insert(mot, nb, cibleMail) :

    index = {}
    if os.path.exists(os.path.join(outputFile4or5, mot[0] + ".json")):
        with open(os.path.join(outputFile4or5, mot[0] + ".json")) as file :
            index = json.load(file)

    if mot in index :
        index[mot].update({cibleMail : nb})
    else :
        value = {mot : {cibleMail : nb}}
        index.update(value)

    with open(os.path.join(outputFile4or5, mot[0] + ".json"), "w") as file :
        json.dump(index, file, indent=4)

def index_less_than_four_letters_insert(mot, nb, cibleMail) :

    index = {}
    if os.path.exists(os.path.join(outputFile4, mot[0] + ".json")):
        with open(os.path.join(outputFile4, mot[0] + ".json")) as file :
            index = json.load(file)

    if mot in index :
        index[mot].update({cibleMail : nb})
    else :
        value = {mot : {cibleMail : nb}}
        index.update(value)

    with open(os.path.join(outputFile4, mot[0] + ".json"), "w") as file :
        json.dump(index, file, indent=4)

def index_more_than_five_letters_insert(mot, nb, cibleMail) :

    index = {}
    if os.path.exists(os.path.join(outputFile5, mot[0] + ".json")):
        with open(os.path.join(outputFile5, mot[0] + ".json")) as file :
            index = json.load(file)

    if mot in index :
        index[mot].update({cibleMail : nb})
    else :
        value = {mot : {cibleMail : nb}}
        index.update(value)

    with open(os.path.join(outputFile5, mot[0] + ".json"), "w") as file :
        json.dump(index, file, indent=4)
total = 0 ;
for folder, subs, files in os.walk(inputFile):
        for mailFile in files:
            total += 1 ;
            print("\rPas de crash ! mail : " + str(total), end="") 
            try :
                cibleMail = os.path.join(folder, mailFile)
                mail = open(cibleMail).read()
                b = email.message_from_string(mail).get_payload()
                msg = email.message_from_file(open(cibleMail))
                if msg['Subject']:
                    Subject = msg['Subject']
                    b = Subject + " " + b
                arr = re.split("\W+", b)
                arr = [mot.lower() for mot in arr]
                counter = collections.Counter(arr)
                for mot,nb in counter.items():
                    if 0 < len(mot) < 4 :
                        index_less_than_four_letters_insert(mot, nb, cibleMail)
                    elif len(mot) > 5 :
                        index_more_than_five_letters_insert(mot, nb, cibleMail)
                    elif 3 < len(mot) < 6 :
                        index_four_or_five_letters_insert(mot,nb, cibleMail)
            except IOError:
                print(IOError)
        print("\n")


