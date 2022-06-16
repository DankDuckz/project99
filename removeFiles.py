import os
import shutil
import time

path = input("Enter the path of your folder")

days = 1
seconds = time.time() - (days*24*60*60)

def getAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if os.path.exists(path):
    print("Path exists")
    for rootFolder, folders, files in os.walk(path):
        for folder in folders:
            folderPath = os.path.join(path,folder)
            if seconds >= getAge(folderPath):
                shutil.rmtree(folderPath)
        
        for file in files:
            filePath = os.path.join(path,file)
            if seconds >= getAge(filePath):
                os.remove(filePath)
else:
    print("Path does not exist")



