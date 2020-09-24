


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)

h = histogram('a')
print(h)

h.get('a', 0)
h.get('b', 0)

def print_hist(h):
    for c in h:
        print (c, h[c])

h = histogram('parrot')
print_hist(h)

print("11.3")

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
print(ValueError)

h = histogram('parrot')
k = reverse_lookup(h, 2)
print(k)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print (hist)

t = [1, 2, 3]
d = dict()
d[t] = 'oops'

print("11.5")

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

hist = histogram('parrot')
print (hist)




















