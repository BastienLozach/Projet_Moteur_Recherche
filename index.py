import email
import os
import json

def get_contact_mails():
    res = {}
    contact_id = 0
    for contact_dir in os.listdir('maildir'):
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

print(json.dumps(get_contact_mails(), indent=4))