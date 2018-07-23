import sys, os, shutil

# newSuffix = str(sys.argv[1])
newSuffix = '.jpg'
title = 'cameraimage'

for index, file in enumerate(os.listdir('./before')):
    oldName = './before/' + str(file)
    newName = './after/' + title + str(index) + newSuffix
    # newName = './after/' + str(file)[:-4] + newSuffix
    shutil.copy2(oldName, newName)
