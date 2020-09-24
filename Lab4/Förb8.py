import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context

url1 = 'http://www.svd.se/'
#file = urllib.request.urlopen(url)
#content = file.read()
#text = content.decode('utf-8')


def find_letters(website,letters):
    try:
        file = urllib.request.urlopen(website)
        content = file.read()
        text = content.decode('utf-8')
        find(letters,text)
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

find("a", "b")




















