import time
import os

from GetURLContent import *

from XMLParseUtils import *
from FileUtils import *

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


def CreateVocabularyXMLCollegiate(keyword, APIKey):
    
    fileName = keyword + '_collegiate.xml'
    if os.path.exists(fileName):
        removeFile(fileName)
    createFile(fileName)
    
    for content in GetURLContentCollegiate(keyword, APIKey):
        appendFile(fileName, content + '\n')


def CreateVocabularyXMLLearners(keyword, APIKey):
    
    fileName = keyword + '_learners.xml'
    removeFile(fileName)
    createFile(fileName)
    
    for content in GetURLContentLearners(keyword, APIKey):
        appendFile(fileName, content + '\n')


def CreateVocabularyXMLIciba(keyword, APIKey):
    
    fileName = keyword + '_iciba.xml'
    removeFile(fileName)
    createFile(fileName)
    
    for content in GetURLContentIciba(keyword, APIKey):
        appendFile(fileName, content + '\n')


def CreateVocabularyXMLYoudao(keyword, APIKey, APIKeyFrom):
    
    fileName = keyword + '_youdao.xml'
    removeFile(fileName)
    createFile(fileName)
    
    for content in GetURLContentYoudao(keyword, APIKey, APIKeyFrom):
        appendFile(fileName, content + '\n')


