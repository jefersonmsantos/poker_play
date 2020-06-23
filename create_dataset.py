import os
from os import path
import shutil

directory = r'/home/jeferson/Documentos/poker_play/img'

for filename in os.listdir(directory):
    filenameSplit = filename.split('-')
    if (path.exists(directory+'/'+filenameSplit[1])=False):
        os.mkdir(directory+'/'+filenameSplit[1]))
    
    shutil.copy(directory + '/' + filename,directory+'/'+filenameSplit[1])


