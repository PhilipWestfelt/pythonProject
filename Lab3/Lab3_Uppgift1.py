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
    return txt

def sort_list_tuples(list1):
    sorted_list = []
    for tuple in list1:
        if len(sorted_list):
            sorted_list.append(tuple)
        else:
            return None

def count_word(txt):
    check_dict = dict()
    word_list = txt.split()
    amount_words = len(word_list)

    for word in word_list:
        if word in check_dict:
            check_dict[word] += 1
        elif word not in check_dict:
            check_dict[word] = 1
    return check_dict,amount_words

def find_max_word(check_dict):
    max_val = 0
    max_tuple = ()
    for key in check_dict:
        if max_val < check_dict[key]:
            max_val = check_dict[key]
            max_tuple = (key,check_dict[key])
    return max_tuple

txt = file2txt(PATH)
No_Signs_Text = remove_signs(txt)
check_dict,amount_words = count_word(No_Signs_Text)
max = find_max_word(check_dict)

print("Total word amount", amount_words)
print("Unique word amount", len(check_dict))
print("Most common word is", "\"",max[0],"\"", "which occurs", max[1], "times.")






