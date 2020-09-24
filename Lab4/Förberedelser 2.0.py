print (3.1, 3.10)


print( int(3.99999))
print(int(-2.3))

print(float(32))


print()


print()


print()



print()

def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)

print(2)
print_twice('Spam')
print_twice('Spam '*4)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'

cat_twice(line1, line2)

print (5.1, 5.7)


quotient = 7 / 3
print(quotient)

remainder = 7 % 3
print(remainder)

print(5 == 5)

print(5 == 6)


x = 53
y = 53
if (x > 0):
    print ('x is positive')


if x < 0:
    pass # need to handle negative values!


if x%2 == 0:
    print ('x is even')
else:
    print ('x is odd')

if x < y:
    print ('x is less than y')
elif x > y:
    print ('x is greater than y')
else:
    print ('x and y are equal')


if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()


if x == y:
    print ('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

