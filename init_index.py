import email
import os
import json
import sys

##parametres

##default
inputFile = "maildir"
outputFile = os.path.join("data","index.json")
##set
if len(sys.argv) >= 2 :
    inputFile = sys.argv[1]
    if len(sys.argv) >= 3 :
        outputFile = sys.argv[2]


def get_contact_mails():
    res = {}
    contact_id = 0
    for contact_dir in os.listdir(inputFile):
        print (contact_id)
        contact_id+=1
        mail_folder = "maildir/" + contact_dir + "/_sent_mail/"
        mail_from = None
        destinataires = []
        if os.path.exists(mail_folder):
            for mail in os.listdir(mail_folder):
                msg = email.message_from_file(open(mail_folder+mail))
                if mail_from is None:
                    mail_from = msg['from']
                if msg['to']:
                    destinataires+=[d.strip() for d in msg['to'].split(",") ]
                if msg['cc']:
                    destinataires+=[d.strip() for d in msg['cc'].split(",") ]
                if msg['cci']:
                    destinataires+=[d.strip() for d in msg['cci'].split(",") ]
            res[mail_from] = {'id': contact_id, 'name': mail_from, 'dest' : destinataires}
    return res

##ecriture du fichier
with open(outputFile, "w") as file :
    file.write(json.dumps(get_contact_mails(), indent=4))

