import re        #Regular Expression
import string
email_chars = string.ascii_letters + string.digits + '.'
testmail1 = "Hej, philip.westfelt@gmail.com är min mailadress"
testmail2 = "Svara till joachim@hotmail.com eller pella@gmail.com"
testmail3 = "Denna sträng innehåller ingen mailadress"
testmail4 = "Denna sträng innehåller @hej men ingen mailadress"
testmail5 = "Lorem Ipsum @is simply dummy text of the printing and@go typesetting"
testmail6 = "Den här mailadressen innehåller åäö@gmail.com vilket betyder att nästa innehåller 123@gmail.com"
testmail7 = "Various versions have evolved over the years åäö@"
testmail8 = "Hej min mail är dag@gmail.com och jag har en annan adress, dag2@hotmail.com och även dag3@outlook.com"



def find_email(text):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)


def test_find_first_email_and_rest():
    testlista = [testmail1,testmail2,testmail3,testmail4,testmail5,testmail6,testmail7,testmail8]
    for test in testlista:
        print(test)
        print(find_email(test))
        print("\n")

test_find_first_email_and_rest()
