import time
import os

from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *
from ParseXMLToContent import *

def CreateFolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def CreateDictFolder(dictname):
    
    timefolder = time.strftime(r"%Y%m%d_%H%M%S", time.localtime())

    DictFoldername = 'xml_' + dictname    
    CreateFolder(DictFoldername)
    os.chdir(DictFoldername)
        
    DictFoldernameDate = dictname + '_' + timefolder  
    CreateFolder(DictFoldernameDate)
    os.chdir(DictFoldernameDate)

if __name__ == '__main__':
    
    dictname = 'momoDict'
    CreateDictFolder(dictname)
    
    index = ['0', '1', '3', '4', '5']
    for item in index:
        fileName = dictname + item + '_collegiate.xml'
        if os.path.exists(fileName):
            removeFile(fileName)
        createFile(fileName)




