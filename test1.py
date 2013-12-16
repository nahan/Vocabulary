test = getPage()
print test

def getPage():
    url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/nerve?key=c24340c1-1b4f-4e9b-8f21-b21a87c88ae8'
    page = urllib.urlopen(url)
    html = page.readlines();
    print "testing"
    return html