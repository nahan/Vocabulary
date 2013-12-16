from FileUtils import *
from MySQLUtils import *

def ResultsToLists():
    
    results0to800 = []
    results801to1600 = []
    results1601to2400 = []
    results2401to3093 = []
    
    results = RetrieveAllWordsFromLongman3000()

    index = 0
    for result in results:
        if index <= 800:
            results0to800.append(result[0])
        elif index > 800 and index <= 1600:
            results801to1600.append(result[0])
        elif index > 1600 and index <= 2400:
            results1601to2400.append(result[0])
        else:
            results2401to3093.append(result[0])
        
        index = index + 1
    
    return results0to800, results801to1600, results1601to2400, results2401to3093