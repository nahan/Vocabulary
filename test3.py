import time
import os
from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *
from ParseXMLToContent import *
from xml.etree import ElementTree

if __name__ == '__main__':
    
    testfile = 'test.xml'

    word_key = []
    word_phonetic = []
    word_acceptation = []
    
    word_key, word_phonetic, word_acceptation = GetContentFromIcibaXML(testfile)
    
    filename = 'test.txt'
    createFile(filename)
    appendFile(filename, '\n')
    for item in word_key:
        appendFile(filename, item + '\n')
    for item in word_phonetic:
        appendFile(filename, item + '\n')
    for item in word_acceptation:
        appendFile(filename, item + '\n')
    
    
    
    
    
    






