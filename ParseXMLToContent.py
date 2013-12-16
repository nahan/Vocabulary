import time
import os
from xml.etree import ElementTree
import xml.dom.minidom as minidom

from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *

def GetContentFromIcibaXML(filename):
    openfile = open(filename).read()
    root = ElementTree.parse(filename)

    #root = ElementTree.fromstring(openfile)
    
    word_key = []
    word_phonetic = []
    word_acceptation = []
    
    children_key = root.findall('key')
    for child in children_key:
        word_key.append(child.text)
    
    children_ps = root.findall('ps')
    for child in children_ps:
        word_phonetic.append(child.text)
    
    children_pos = root.findall('pos')
    children_acceptation = root.findall('acceptation')
    for i in range(0, len(children_pos)):
        word_acceptation.append(children_pos[i].text + ' ' + children_acceptation[i].text.replace('\n', ''))
    
    return word_key, word_phonetic, word_acceptation

def CreateIcibaVocabularyText():
    
    rootPath = os.getcwd()
    dictfoldername = 'xml_iciba'
    os.chdir(dictfoldername)    
    
    dictfolderpath = os.getcwd()
    templist = os.listdir(dictfolderpath)
    latestVocabularyFolder = templist[len(templist) - 1]
    latestVocabularyList = os.listdir(latestVocabularyFolder)
    
    os.chdir(latestVocabularyFolder)
    for item in latestVocabularyList:
        #print item
        filename = 'Vocabulary.txt'
        if not os.path.exists(filename):
            createFile(filename)
        
        word_key = []
        word_phonetic = []
        word_acceptation = []
        word_key, word_phonetic, word_acceptation = GetContentFromIcibaXML(item)  
        
        for item in word_key:
            appendFile(filename, item + '\n')
        for item in word_phonetic:
            appendFile(filename, item + '\n')
        for item in word_acceptation:
            appendFile(filename, item + '\n')
        
        appendFile(filename, '\n')
       
    os.chdir(rootPath)
    

