a2 = int(input('add a2 '))
a1 = int(input('add a1 '))
b2 = int(input('add b2 '))
b1 = int(input('add b1 '))

c2 = a2 + b2 + (a1 + b1) // 10
c1 = (a1 + b1) % 10

print(c2, c1)
