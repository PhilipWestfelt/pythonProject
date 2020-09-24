

import random
from Uppgift3 import bubblesort

def randomlist(number):
    list = [0] * number
    for element in range(len(list)):
        list[element] = random.randint(0, 100)
    return list

def sortrandomlist(number):
    list = randomlist(number)
    print(list)
    sortedlist = bubblesort(list)
    print(sortedlist)


sortrandomlist(10)

