import time

from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *
from ParseXMLToContent import *

def WebsterDictCollegiate():
    
    APIKeyCollegiate01 = 'c24340c1-1b4f-4e9b-8f21-b21a87c88ae8'
    APIKeyCollegiate02 = '8e6168cb-5210-40a5-93d8-ac5fb42e6b7b'
    APIKeyCollegiate03 = '28dbb84b-2d2a-48ea-93e1-45023d4fe6ce'
    APIKeyCollegiate04 = 'a1ac40ba-22f5-4749-bd44-ca0b262bf4c3'
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    
    list1, list2, list3, list4 = ResultsToLists()
    
    rootFolder = os.getcwd()
    CreateDictFolder('webster_collegiate')
    
    for item in list1:
        CreateVocabularyXMLCollegiate(item, APIKeyCollegiate01)
    for item in list2:
        CreateVocabularyXMLCollegiate(item, APIKeyCollegiate02)
    for item in list3:
        CreateVocabularyXMLCollegiate(item, APIKeyCollegiate03)
    for item in list4:
        CreateVocabularyXMLCollegiate(item, APIKeyCollegiate04)
    
    os.chdir(rootFolder)

def WebsterDictLearners():
    
    APIKeyLearners01 = '622adff2-ff1e-4e09-b64b-95576895a146'
    APIKeyLearners02 = '5d55a2e0-2570-49da-b8dd-480f4773a794'
    APIKeyLearners03 = '1c4e050d-853e-40bb-a76c-360a9827a62e'
    APIKeyLearners04 = 'f88cf103-b8af-497c-be51-8b8ebd834906'
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    
    list1, list2, list3, list4 = ResultsToLists()
    
    rootFolder = os.getcwd()
    CreateDictFolder('webster_learners')
    
    for item in list1:
        CreateVocabularyXMLLearners(item, APIKeyLearners01)
    for item in list2:
        CreateVocabularyXMLLearners(item, APIKeyLearners02)
    for item in list3:
        CreateVocabularyXMLLearners(item, APIKeyLearners03)
    for item in list4:
        CreateVocabularyXMLLearners(item, APIKeyLearners04)
    
    os.chdir(rootFolder)
    
def IcibaDict():
    
    APIKeyIciba = '47AE6C01E17C9F42465073F9A7A7F4FA'
    
    allList = ResultsToList()
    
    rootFolder = os.getcwd()
    CreateDictFolder('iciba')
    
    for item in allList:
        CreateVocabularyXMLIciba(item, APIKeyIciba)
    
    os.chdir(rootFolder)

def YoudaoDict():
    
    APIKeyYoudao01 = '1351200996'
    APIKeyFrom01 = 'holyenglish'
    
    APIKeyYoudao02 = '1207294357'
    APIKeyFrom02 = 'abcBook'
    
    APIKeyYoudao03 = '1589834718'
    APIKeyFrom03 = 'xyzBook'
    
    APIKeyYoudao04 = '1986011872'
    APIKeyFrom04 = '678Book'
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    
    list1, list2, list3, list4 = ResultsToLists()
    
    rootFolder = os.getcwd()
    CreateDictFolder('youdao')
    
    for item in list1:
        CreateVocabularyXMLYoudao(item, APIKeyYoudao01, APIKeyFrom01)
    #time.sleep(3600)
    
    for item in list2:
        CreateVocabularyXMLYoudao(item, APIKeyYoudao02, APIKeyFrom02)
    #time.sleep(3600)
    
    for item in list3:
        CreateVocabularyXMLYoudao(item, APIKeyYoudao03, APIKeyFrom03)
    #time.sleep(3600)
    
    for item in list4:
        CreateVocabularyXMLYoudao(item, APIKeyYoudao04, APIKeyFrom04)
    
    os.chdir(rootFolder)


if __name__ == '__main__':
    
    print '****************************************************************'
    print '*                       Program Starting                       *'
    print '****************************************************************'
    print ''
    
    
    #YoudaoDict()
    #WebsterDictLearners()
    #IcibaDict()
    
    #CreateIcibaVocabularyText()
    #InsertIcibaVocabularyContentIntoDB()
    
    
    #for i in range(0, 22):
    #    time.sleep(0.5)
    #    print '->',
    #
    #
    #time.sleep(5)
    #print ''
    #print ''
    #time.sleep(5)
    print '****************************************************************'
    print '*                        Program Ended                         *'
    print '****************************************************************'
    



