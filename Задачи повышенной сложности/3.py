a3 = int(input('add a3 '))
a2 = int(input('add a2 '))
a1 = int(input('add a1 '))
b3 = int(input('add b3 '))
b2 = int(input('add b2 '))
b1 = int(input('add b1 '))

c3 = a3+b3 + ((a2+b2 + (a1+b1)//10) // 10)
c2 = (a2 + b2 + (a1 + b1) // 10) % 10
c1 = (a1 + b1) % 10

print(c3, c2, c1)
