import random
a = int(input('a = '))
b = int(input('b = '))
if a%b==0 or b%a==0:
    print('1')
else:
    print(random.randint(0, 10))
