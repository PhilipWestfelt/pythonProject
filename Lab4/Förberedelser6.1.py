import math


def distance(x1, y1, x2, y2):
    return 0.0

print(distance(1, 2, 4, 6))


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print ('dx is', dx)
    print ('dy is', dy)
    return 0.0

print(distance(1, 2, 4, 6))


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    print ('dsquared is: ', dsquared)
    return 0.0

print(distance(1, 2, 4, 6))


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

print(distance(1, 2, 4, 6))


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


a = is_divisible(10, 18)
print(a, a+2)



bruce = 5
print (bruce,)
bruce = 7
print (bruce)


a = 5
b = a       # a and b are now equal
a = 3       # a and b are no longer equal

x = 0
x = x + 1
print()

def sequence(n):
    while n != 1:
        print (n,)
        if n%2 == 0:        # n is even
            n = n/2
        else:               # n is odd
            n = n*3+1

print (sequence(10))

def countdown(n):
    while n > 0:
        print (n)
        n = n-1
    print ('Blastoff!')

print (countdown(10))


i = 0
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    print("fib(",n,"-1)", "fib(",n,"-2)")
    return fib(n-1) + fib(n-2)

fibcache = {}
def  sum_fibonacci(n):
    """Compute the nth Fibonacci number.

    >>> sum_fibonacci(35)
    9227465
    >>> sum_fibonacci(10)
    55
    >>> sum_fibonacci(0)
    0
    >>> sum_fibonacci(1)
    1
    >>> sum_fibonacci(5)
    5
    """
    if n == 0:
        fibcache[n] = 0
        return fibcache[n]
    elif n == 1:
        fibcache[n] = 1
        return fibcache[n]
    else:
        sum_left = 0
        sum_right = 0
        if n-2 in fibcache.keys():
            sum_left += fibcache[n-2]
        else:
            sum_left += sum_fibonacci(n-2)
            print( "fib(", n, "-2)")

            fibcache[n-2] = sum_left
        if n-1 in fibcache.keys():
            sum_right += fibcache[n-1]
        else:
            sum_right += sum_fibonacci(n-1)
            print("fib(", n, "-1)")
            fibcache[n-1] = sum_right
        return sum_left + sum_right
kaka = [1,2,3,4,6,7]
sum = 0

def summa_lista(i,l,sum):
    if(i> len(l)-1):
        return sum
    else:
        print(l[i],"summa=>",sum)
        sum = sum + l[i]
        return summa_lista(i+1,l,sum)

a = summa_lista(0,kaka,0)
print(a)


def summerinio(lista):
    sum = 0
    for i in lista:
        sum = i+sum
    return sum

print(summerinio([9,5,13,32,73,4,5]))


