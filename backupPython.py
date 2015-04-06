#this is hai branch
import os
import sys
import shutil
from datetime import datetime

# path to download folder
path = "/Users/hai/Downloads"
dirs = os.listdir(path)

#get current date
date = datetime.now().date()
print(date)

#prepare archive folder name
archieve = "backup-" + date.strftime('%m%d%Y')

#full path archieve folder
destination = "/".join((path,archieve))


#check folder exists
if os.path.exists(destination):
    sys.exit("Folder Exists.")
#create folder archive
else:
    folder = os.makedirs(destination)

#file count
count = 0;

# Write files in directory to zip
for file in dirs:
    tempSource = "/".join((path,file))
    tempDestination = "/".join((destination,file))
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        print ("Time : " + currentTime + "\n")
        print ("File Transfer: " + file + "\n")
        shutil.move(tempSource,tempDestination)
        count = count + 1

    except: print("Error")

currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print ("Time : " + currentTime + "\n")
print ("%s files had been successfully transfered." %(count))
