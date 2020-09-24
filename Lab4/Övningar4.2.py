import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context
url1 = 'http://www.kattbajs.se/'
url2 = 'http://www.svd.se/'
#file = urllib.request.urlopen(url)
#content = file.read()
#text = content.decode('utf-8')


def name(website,leaders):
    try:
        file = urllib.request.urlopen(website)
        content = file.read()
        text = content.decode('utf-8')
        amount_mentions(leaders,text)
    except Exception as e:
        print(e)
        return False



def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
    index = index + 1
    return -1


leaders = ["Trump", "Macron", "Putin"]

name(url2,leaders)













