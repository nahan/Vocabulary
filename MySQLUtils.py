import MySQLdb

def CreateWords():
    print 'CreateWords'


def RetrieveAllWordsFromLongman3000():
    
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='1234',db='longman3000',port=3306)
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