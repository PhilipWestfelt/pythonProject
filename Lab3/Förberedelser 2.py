import os

def file2txt():
    with open("output.txt") as file:
        data = file.read()
        print(data)
        return data

txt =file2txt()
if "h" in txt:
    print("dad")
x = "banan"
a = "c" in x
print(a,"ads")

def checke(char,word):
   for i in range (0,len(word)):
        if word[i] == char:
            return True

   return False

print(checke("a",x))


s = 'Monty Python'

print (s[0:5])

print (s[6:12])

fruit = 'banana'
print (fruit[:3])
print (fruit[3:])

print (fruit[:])
print (fruit[:9])


greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print (new_greeting)
print (greeting)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
print(123)
word = 'Banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print (count)

word = 'banana'
new_word = word.upper()
print (new_word)

word = 'banana'
index = word.find('na', 3)
print (index)

'a' in 'banana'

'seed' in 'banana'


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print (letter)

