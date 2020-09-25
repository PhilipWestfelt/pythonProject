import re        #Regular Expression
import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context
url1 = 'http://www.svt.se/'
url2 = 'http://www.it.uu.se/katalog/bylastname/'
url3 = 'http://user.it.uu.se/~joachim/'
url4 = 'http://www.imdb.com/'
url5 = 'http://www.svd.se/'
url6 = 'Fredag'
url7 = 'https://www.polisen.se/'
url8 = ''


def text_search(website):
    try:
        file = urllib.request.urlopen(website)
        content = file.read()
        text = content.decode('utf-8')
        text = text.replace("'", " ").replace('"', " ")
        mail = find_email(text)
        links = find_links(text)
        results = mail
        choice = input("Write 1 for maillist or 2 for linklist: ")
        if choice == "2":
            results = links
        return results
    except Exception as e:
        print("Exception error", (e))
        return False



def find_email(text):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z0-9-.]+)", text)

def find_links(text):
    return re.findall("([w][w][w]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)


def remove_duplicates(duplicate_list):
    return list(dict.fromkeys(duplicate_list))


def print_list(list):
    for results in list:
        print(results)


list2 = text_search(url2)
print_list(list2)
print("Remove duplicates")
list2 = remove_duplicates(list2)
print_list(list2)



