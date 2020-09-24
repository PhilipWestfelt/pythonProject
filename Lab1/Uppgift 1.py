

def sum_digits(n):
    sum = 0
    if(n>0):
        while n:
            sum= sum+n % 10
            n //= 10
    return sum
num = 1338
print(sum_digits(num))






