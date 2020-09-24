import string
email_chains = string.ascii_letters + string.digits + '.'
testmail1 = "Hej, philip.westfelt@gmail.com är min mailadress"
testmail2 = "svara till joachim@hotmailö.com eller pella@gmail.com"
testmail3 = "Denna sträng innehåller ingen mailadress"
testmail4 = "Denna sträng innehåller @hej men ingen mailadress"


def find_name_start(text, at_index):
    first_index = 0
    for index in range(at_index -1, -1, -1): #baklänges!
        if text[index] not in email_chains:
            first_index = index + 1
            break
    return first_index

def find_name_end(text, at_index):
    second_index = at_index
    for index in range(at_index+1, len(text)+1):
        if text[index] not in email_chains:
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


def test_find_first_email_and_rest():
    testmail1 = "Hej, philip.westfelt@gmail.com är min mailadress"
    print(find_first_email_and_rest(testmail1))
    testmail2 = "svara till joachim@hotmail.com eller pella@gmail.com"
    print(find_first_email_and_rest(testmail2))
    testmail3 = "Denna sträng innehåller ingen mailadress"
    print(find_first_email_and_rest(testmail3))
    testmail4 = "Denna sträng innehåller @hej men ingen mailadress"
    print(find_first_email_and_rest(testmail4))
    testmail5 = "Hej, philip.westfelt@gmail.com är min mailadress"
    print(find_first_email_and_rest(testmail5))
    testmail6 = "Den här mailadressen innehåller åäö@gmail.com vilket betyder att nästa innehåller 123@gmail.com"
    print(find_first_email_and_rest(testmail6))
    testmail7 = "Denna sträng innehåller ingen mailadress"
    print(find_first_email_and_rest(testmail7))
    testmail8 = "Denna sträng innehåller @hej men ingen mailadress"
    print(find_first_email_and_rest(testmail8))

test_find_first_email_and_rest()
