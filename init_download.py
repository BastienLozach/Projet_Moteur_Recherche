import os
import sys
import urllib.request

import gzip
import shutil
import tarfile

mailDirectory = "maildir"

##link
link = "https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz"
archiveName = "enron_mail_20150507.tar.gz"

##download
if not os.path.exists(archiveName):
    urllib.request.urlretrieve(link, archiveName)

##extract
##https://stackoverflow.com/a/30888321
if not os.path.exists(mailDirectory):
    if (archiveName.endswith("tar.gz")):
        tar = tarfile.open(archiveName, "r:gz")
        tar.extractall()
        tar.close()
    elif (archiveName.endswith("tar")):
        tar = tarfile.open(archiveName, "r:")
        tar.extractall()
        tar.close()

