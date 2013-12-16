import urllib


def GetURLContentCollegiate(keyword, APIKey):
    url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/%s?key=%s" % (keyword, APIKey)
    page = urllib.urlopen(url)
    html = page.readlines();
    return html

def GetURLContentLearners(keyword, APIKey):
    url = "http://www.dictionaryapi.com/api/v1/references/learners/xml/%s?key=%s" % (keyword, APIKey)
    page = urllib.urlopen(url)
    html = page.readlines();
    return html