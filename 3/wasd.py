def square(x):
    return x*x

from math import sqrt
def hypotenusa(a,b):
    c = sqrt(square(a)+square(b))
    return c

print(hypotenusa(3,4))
print(hypotenusa(0,7))
print(hypotenusa(5,12))
a = hypotenusa(3,4)
print(a+1)
print(a)
a = a+1
print(a)
b = [1,2,3,4,5,6]
for fing in b:
    print(fing)