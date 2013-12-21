import MySQLdb

def CreateWords():
    print 'CreateWords'


def RetrieveAllWordsFromLongman3000():
    
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='1234', db='longman3000', port=3306)
        cur = conn.cursor()
        cur.execute('SELECT word FROM vocabulary')
        
        results = cur.fetchall()

        cur.close()
        conn.close()
        
        return results
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def UpdateWords():
    print 'UpdateWords'


def DeleteWords():
    print 'DeleteWords'

"""update vocabulary_test set word_phonetic="this is a test" where word='abandon';"""
def UpdateWordWithPhoneticAndParaphraseCN(word, phonetic, paraphraseCN):
    
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='1234', db='longman3000_test', charset='utf8', port=3306)
        cur = conn.cursor()
        update_sql = 'update vocabulary_test set word_phonetic="%s", word_paraphrase_cn="%s" where word="%s"' % (phonetic, paraphraseCN, word)
        cur.execute(update_sql)
        
        conn.commit()
        cur.close()
        conn.close()
        
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
