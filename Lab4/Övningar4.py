import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context
url1 = 'http://www.kattbajs.se/'
url2 = 'http://www.dn.se/'
#file = urllib.request.urlopen(url)
#content = file.read()
#text = content.decode('utf-8')


def das_open(website):
    try:
        file = urllib.request.urlopen(website)
        return True
    except Exception as e:
        print(e)
        return False


a =das_open(url2)
print(a)


def maths():
    n = input("siffra?")
    a = [1,2,3,5]
    try:
        print(a[int(n)])
    except Exception as e:
        print(e)
        print("du får inte dela med eller bokstav",n)
        maths()
maths()
















