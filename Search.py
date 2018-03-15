import email
import os
import json
import sys

##default
inputFile = "maildir"
inputFile2 = ""
outputFile = "data/index.json"

def get_search():
    res = {}
    le_dossier = 0
    le_sous_dossier = 0
    
    for dossier in os.listdir(inputFile):
        inputFile2 = inputFile + "/" + dossier
        le_dossier+= 1
        for sous_dossier in os.listdir(inputFile2):
            le_sous_dossier+=1
            mail_folder = "maildir/" + dossier +"/"+ sous_dossier
            #print (mail_folder)
            test = open("maildir/allen-p/discussion_threads/1_").read()
            b = email.message_from_string(test).get_payload()
            print (b)
            if b.find('in') != -1:
                print ("trouve")
            else:
                print ("Pas trouve")
    return le_sous_dossier


print (get_search())