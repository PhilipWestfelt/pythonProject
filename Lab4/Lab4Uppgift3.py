import re        #Regular Expression
import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context
url1 = 'http://www.dn.se/'
url2 = 'http://www.it.uu.se/katalog/bylastname/'
url3 = ''


def name(website):
    try:
        file = urllib.request.urlopen(website)
        content = file.read()
        text = content.decode('utf-8')
        text = text.replace("'", " ").replace('"', " ")
        mail1 = find_email(text)
        links = find_links(text)
        mail = mail1
        choice = input("Skriv 1 för mail o 2 för links: ")
        if choice == "2":
            mail = links
        return mail
    except Exception as e:
        print(e)
        return False

def find_email(text):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)

def find_links(text):
    return re.findall("([www]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)

def

print(name(url2))







