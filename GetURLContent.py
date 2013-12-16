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

def GetURLContentIciba(keyword, APIKey):
    url = "http://dict-co.iciba.com/api/dictionary.php?w=%s&key=%s" % (keyword, APIKey)
    page = urllib.urlopen(url)
    html = page.readlines();
    return html

def GetURLContentYoudao(keyword, APIKey, APIKeyFrom):
    url = "http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=xml&version=1.1&q=%s" % (APIKeyFrom, APIKey, keyword)
    page = urllib.urlopen(url)
    html = page.readlines();
    return html