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

def moreThan5() :
    index = {}
    total = 0 ;
    for folder, subs, files in os.walk(inputFile):
        for mailFile in files :
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
                    if len(mot) > 5 :
                        if not mot[0] in index :
                            index[mot[0]] = {}
                        if mot in index[mot[0]] :
                            index[mot[0]][mot].update({cibleMail : nb})
                        else :
                            value = {mot : {cibleMail : nb}}
                            index[mot[0]].update(value)
            except IOError:
                a = "do nothing"
            except UnicodeDecodeError:
                a = "do nothing"
    print("\n")

    for letter in index :
        with open(os.path.join(outputFile5, letter + ".json"), "w") as file :
            json.dump(index[letter], file, indent=4)

def lessThan4() :
    index = {}
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
                        if not mot[0] in index :
                            index[mot[0]] = {}
                        if mot in index[mot[0]] :
                            index[mot[0]][mot].update({cibleMail : nb})
                        else :
                            value = {mot : {cibleMail : nb}}
                            index[mot[0]].update(value)
            except IOError:
                a = "do nothing"
            except UnicodeDecodeError:
                a = "do nothing"
    print("\n")

    for letter in index :
        with open(os.path.join(outputFile4, letter + ".json"), "w") as file :
            json.dump(index[letter], file, indent=4)


def between4and5() :
    index = {}
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
                    if  4 <= len(mot) <= 5 :
                        if not mot[0] in index :
                            index[mot[0]] = {}
                        if mot in index[mot[0]] :
                            index[mot[0]][mot].update({cibleMail : nb})
                        else :
                            value = {mot : {cibleMail : nb}}
                            index[mot[0]].update(value)
            except IOError:
                a = "do nothing"
            except UnicodeDecodeError:
                a = "do nothing"
    print("\n")

    for letter in index :
        with open(os.path.join(outputFile4or5, letter + ".json"), "w") as file :
            json.dump(index[letter], file, indent=4)


print("Plus de 5")
moreThan5()

print("moins de 4")
lessThan4()

print("4 et 5")
between4and5()
