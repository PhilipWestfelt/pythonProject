

from Uppgift1 import is_sorted

def bubblesort(li):
    point_counter = 0
    while not(is_sorted(li)):
        for k in range(len(li) - 1):
            byte = bytintill(li,k)
            if byte == True:
                point_counter += 1
    print(point_counter, 'byten har skett')
    return li

def bytintill(li,k):
    if li[k] > li[k + 1]:
        li[k], li[k+1] = li[k + 1], li[k]
        return True
    else:
        return False
