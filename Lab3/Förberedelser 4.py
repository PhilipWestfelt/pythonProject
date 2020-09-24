
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)


t = ['a', 'b', 'c']
del t[0]
print(t)


t = ['a', 'b', 'c']
t.remove('b')
print(t)


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:4]
print(t)

print("10.9")

s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
print(s)


t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)


print("11.1-11.5")

eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

print (eng2sp['two'])


len(eng2sp)
'one' in eng2sp
'uno' in eng2sp


