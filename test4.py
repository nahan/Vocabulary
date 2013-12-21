import time
import os
from GetURLContent import *
from XMLParseUtils import *
from FileUtils import *
from CreateVocabularyXML import *
from MySQLUtils import *
from VocabularyResultsToList import *
from ParseXMLToContent import *

if __name__ == '__main__':
    
    #UpdateWordWithPhoneticAndParaphraseCN('abandon', 'phonetic', 'paraphrase')

    InsertIcibaVocabularyContentIntoDB()
    
    






