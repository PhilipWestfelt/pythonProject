import operator
import string
import os
PATH = "Sherlock.txt"

def file2txt(path):
    with open(path) as file:
        data = file.read()
    return data


def remove_signs(txt):
    txt = txt.replace(".", "")
    txt = txt.replace(",", "")
    txt = txt.replace("\"", "")
    txt = txt.replace("!","")
    txt = txt.replace("?","")
    txt = txt.lower()
    word_list = txt.split()

    return word_list

def count_word(list):
    check_dict = dict()


    for word in list:
        if word in check_dict:
            check_dict[word] += 1
        elif word not in check_dict:
            check_dict[word] = 1
    return check_dict

def find_max_word(check_dict):
    max_val = 0
    max_tuple = ()
    for key in check_dict:
        if max_val < check_dict[key]:
            max_val = check_dict[key]
            max_tuple = (key, check_dict[key])
    return max_tuple


def following_max_word(word_list):
    following_max = 0
    following_max_tuple = ()
    for key in word_list:
        if max_val < word_list[key]:
            max_val = word_list[key]
            following_max_tuple = (key, word_list[key])
    return following_max_tuple

def words_after(lookup_word,word_list):
    lookup_word_list = []
    for i, word in enumerate(word_list):
        if word == lookup_word:
            print(i)
            if word_list[i+1] != None:
                lookup_word_list.append(word_list[i+1])
    return lookup_word_list

txt = file2txt(PATH)
word_list = remove_signs(txt)
check_dict = count_word(word_list)
max1 = find_max_word(check_dict)
the_afterlist = words_after(word_list)
the_dict = count_word(the_afterlist)
max2 = find_max_word(the_dict)

print(the_dict)
print(max2)
print("Total word amount", len(word_list))
print("Unique word amount", len(check_dict))
print("Most common word is", "\"",max1[0],"\"", "which occurs", max1[1], "times.")
print("Most common word following", "\"",max1[0],"\"", "is", "which occurs", "times.")















