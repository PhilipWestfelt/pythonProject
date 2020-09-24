print("11.5")

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res



t = ('a', 'b', 'c', 'd', 'e')
t1 = 'a',
type(t1)
print(t1)

t2 = ('a')
type(t2)
print(t2)

t = tuple()
print(t)

t = tuple('lupins')
print(t)


t = ('a', 'b', 'c', 'd', 'e')

print (t[0])
print (t[1:3])
t = ('A',) + t[1:]
print(t)

a = 1
b = 8

temp = a
a = b
b = temp

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print(domain)

t = divmod(7, 3)
print(t)

quot, rem = divmod(7, 3)
print(quot)
print(rem)
print("18.8")
def min_max(t):
    return min(t), max(t)

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

