import time

from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *

if __name__ == '__main__':
    
    APIKeyCollegiate01 = 'c24340c1-1b4f-4e9b-8f21-b21a87c88ae8'
    APIKeyCollegiate02 = '8e6168cb-5210-40a5-93d8-ac5fb42e6b7b'
    APIKeyCollegiate03 = '28dbb84b-2d2a-48ea-93e1-45023d4fe6ce'
    APIKeyCollegiate04 = 'a1ac40ba-22f5-4749-bd44-ca0b262bf4c3'
    
    APIKeyLearners01 = '622adff2-ff1e-4e09-b64b-95576895a146'
    APIKeyLearners02 = '5d55a2e0-2570-49da-b8dd-480f4773a794'
    APIKeyLearners03 = '1c4e050d-853e-40bb-a76c-360a9827a62e'
    APIKeyLearners04 = 'f88cf103-b8af-497c-be51-8b8ebd834906'
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    
    list1, list2, list3, list4 = ResultsToLists()
    
    for item in list1:
        CreateVocabularyXMLLearners(item, APIKeyLearners01)
        time.sleep(60)
    for item in list2:
        CreateVocabularyXMLLearners(item, APIKeyLearners02)
        time.sleep(20)
    for item in list3:
        CreateVocabularyXMLLearners(item, APIKeyLearners03)
        time.sleep(20)
    for item in list4:
        CreateVocabularyXMLLearners(item, APIKeyLearners04)
        time.sleep(20)
    
    #for item in list1:
    #    GetURLContentCollegiate(item, APIKeyCollegiate01)
    #for item in list2:
    #    GetURLContentCollegiate(item, APIKeyCollegiate02)
    #for item in list3:
    #    GetURLContentCollegiate(item, APIKeyCollegiate03)
    #for item in list4:
    #    GetURLContentCollegiate(item, APIKeyCollegiate04)



