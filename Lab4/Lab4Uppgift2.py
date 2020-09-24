import re
import string
email_chars = string.ascii_letters + string.digits + '.'
testmail1 = "Hej, philip.westfelt@gmail.com är min mailadress"
testmail2 = "Svara till joachim@hotmail.com eller pella@gmail.com"
testmail3 = "Denna sträng innehåller ingen mailadress"
testmail4 = "Denna sträng innehåller @hej men ingen mailadress"
testmail5 = "Lorem Ipsum @is simply dummy text of the printing and@go typesetting"
testmail6 = "Den här mailadressen innehåller åäö@gmail.com vilket betyder att nästa innehåller 123@gmail.com"
testmail7 = "Various versions have evolved over the years åäö@"

def find_name_start(text, at_index):
    first_index = 0
    for index in range(at_index -1, -1, -1): #baklänges!
        if text[index] not in email_chars:
            first_index = index + 1
            break
    return first_index

def find_name_end(text, at_index):
    second_index = at_index
    for index in range(at_index+1, len(text)+1):
        if text[index] not in email_chars :
            second_index = index + 1
            break
    return second_index

def find_first_email_and_rest(text):
    at_index = text.find('@')
    if at_index < 0:
        return None, None
    name_start = find_name_start(text, at_index)
    if name_start == at_index:
        return None, text[at_index+1:len(text)]
    name_end = find_name_end(text, at_index)
    if name_end == at_index:
        return None, text[at_index+1:len(text)]
    return text[name_start: name_end], text[name_end:len(text)]


def find_email(text):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)


def test_find_first_email_and_rest():
    testlista = [testmail1,testmail2,testmail3,testmail4,testmail5,testmail6,testmail7]
    for test in testlista:
        print(test)
        print(find_email(test))
        print("\n")

test_find_first_email_and_rest()
