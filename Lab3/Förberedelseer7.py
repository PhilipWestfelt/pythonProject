print("14.1, 14.2, 14.4")




fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land.\n"
fout.write(line2)


fout.close()
fout.close()

import os
cwd = os.getcwd()
print (cwd)

os.path.abspath('memo.txt')

os.path.exists('memo.txt')

os.path.isdir('memo.txt')

os.path.isdir('music')


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
    if os.path.isfile(path):
        print (path)
    else:
        walk(path)

print(walk)




