

def initial(namn):
    i = 0

    if "-" in namn:
        namn = namn.replace("-","  ")

    name_list = namn.split()
    initialklar = ''
    for antal in range(len(name_list)):
        initialklar += name_list[antal][0] + '.'
    return initialklar


def test2():
    namn1 = 'Philip Nathorst-Westfelt'
    print(initial(namn1))
    namn2 = 'Daniel Svensson '
    print(initial(namn2))
    namn3 = 'Karl Daniel Sjöström'
    print(initial(namn3))

test2()






