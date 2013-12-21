import time
import os
import xml.dom.minidom as minidom
import shutil

from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *

def GetContentFromIcibaXML(filename):
    
    xmlFile = minidom.parse(filename) 
    xmlRoot = xmlFile.documentElement

    word_key = []
    word_phonetic = []
    word_phonetic_bre = ''
    word_phonetic_ame = ''
    word_acceptation = []
    word_acceptation_all = ''
    
    node_key = xmlRoot.getElementsByTagName('key')
    for item in node_key:
        word_key.append(GetText(item).replace('\n', ''))
    
    node_phonetic = xmlRoot.getElementsByTagName('ps')
    for item in node_phonetic:
        word_phonetic.append('[' + GetText(item).replace('\n', '') + ']')  
    if len(word_phonetic) == 2:
        word_phonetic_bre += 'BrE.' + word_phonetic[0]
        word_phonetic_ame += 'AmE.' + word_phonetic[1]
    word_phonetic.append(word_phonetic_bre + ' ' + word_phonetic_ame)
    
    node_property = xmlRoot.getElementsByTagName('pos')
    node_acceptation = xmlRoot.getElementsByTagName('acceptation')
    for index in range(0, len(node_property)):
        word_acceptation.append(GetText(node_property[index]).replace('\n', '') + ' ' + GetText(node_acceptation[index]).replace('\n', ''))
        word_acceptation_all += GetText(node_property[index]).replace('\n', '') + ' ' + GetText(node_acceptation[index]).replace('\n', '') + ' '
    word_acceptation.append(word_acceptation_all)
    return word_key, word_phonetic, word_acceptation

def CreateIcibaVocabularyText():
    
    rootPath = os.getcwd()
    
    filename = 'iciba_Vocabulary.txt'
    if os.path.exists(filename):
        removeFile(filename)
    createFile(filename)
    
    filePath = os.path.join(rootPath, filename)
    
    dictfoldername = 'xml_iciba'
    dictfolderPath = os.path.join(rootPath, dictfoldername)
    
    dictfolderList = os.listdir(dictfolderPath)
    latestVocabularyFolder = dictfolderList[len(dictfolderList) - 1]
    latestVocabularyFolderPath = os.path.join(dictfolderPath, latestVocabularyFolder)
    latestVocabularyList = os.listdir(latestVocabularyFolderPath)
    for item in latestVocabularyList:
        
        if item.endswith('txt'):
            continue
        
        word_key = []
        word_phonetic = []
        word_acceptation = []
        word_key, word_phonetic, word_acceptation = GetContentFromIcibaXML(os.path.join(latestVocabularyFolderPath,item))  
        
        appendFile(filename, word_key[len(word_key) - 1] + '\n')
        appendFile(filename, word_phonetic[len(word_phonetic) - 1] + '\n')
        appendFile(filename, word_acceptation[len(word_acceptation) - 1] + '\n')
        
        """
        for item in word_key:
            appendFile(filename, item + '\n')
        for item in word_phonetic:
            appendFile(filename, item + '\n')
        for item in word_acceptation:
            appendFile(filename, item + '\n')
        """
        
        appendFile(filename, '\n')
    
    shutil.copyfile(filePath, os.path.join(latestVocabularyFolderPath, 'iciba_Vocabulary.txt'))
    removeFile(filePath)

def InsertIcibaVocabularyContentIntoDB():
    
    rootPath = os.getcwd()
    
    dictfoldername = 'xml_iciba'
    dictfolderPath = os.path.join(rootPath, dictfoldername)
    
    dictfolderList = os.listdir(dictfolderPath)
    latestVocabularyFolder = dictfolderList[len(dictfolderList) - 1]
    latestVocabularyFolderPath = os.path.join(dictfolderPath, latestVocabularyFolder)
    latestVocabularyList = os.listdir(latestVocabularyFolderPath)
    for item in latestVocabularyList:
        
        if item.endswith('txt'):
            continue
        
        word_key = []
        word_phonetic = []
        word_acceptation = []
        word_key, word_phonetic, word_acceptation = GetContentFromIcibaXML(os.path.join(latestVocabularyFolderPath,item))
        
        UpdateWordWithPhoneticAndParaphraseCN(word_key[len(word_key) - 1], word_phonetic[len(word_phonetic) - 1], word_acceptation[len(word_acceptation) - 1])
        







