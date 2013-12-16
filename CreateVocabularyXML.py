from GetURLContent import *

from XMLParseUtils import *
from FileUtils import *

def CreateVocabularyXMLCollegiate(keyword, APIKey):
    fileName = keyword + '_collegiate.xml'
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


