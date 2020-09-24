

def is_sorted(lista):
    flagga = True
    for siffra in range(len(lista)-1):
        if lista[siffra] <= lista[siffra+1]:
            större = True
        else:
            större = False
            break
    return större

def test1():
    lista1 = (1,0,0,0,0,0)
    print(is_sorted(lista1))
    lista2 = (1,7,18,33,34,59)
    print(is_sorted(lista2))
    lista3 = (9,0,7,3,5,1)
    print(is_sorted(lista3))
    lista3 = (1,1,2,3,5,9)
    print(is_sorted(lista3))

test1()











