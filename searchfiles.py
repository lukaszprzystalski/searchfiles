import os
import time

'''
script lists all files with given extension in given directory.
Additionally it can print modification date of those files
'''

path = 'C:\\'

def searchFiles(extension):
    for root, dirs, files in os.walk(path):
        for file in files:      
            if file.endswith('.' + extension):
                filepath = os.path.join(root, file)
                modDate = time.ctime(os.path.getmtime(filepath))
                print(os.path.join(root, file))
                print(file, modDate)

searchFiles('exe')