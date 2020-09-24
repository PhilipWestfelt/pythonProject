

def integer(n):
    while(n!=1):
        if(n%2==0 and n!=1):
            print(n)
            print("First loop")
            n = n/2
        if(n%2!=0 and n!=1):
            print(n)
            print("Second loop")
            a = n
            n = 3*a+1
    return(n)
num = 6
integer(num)


