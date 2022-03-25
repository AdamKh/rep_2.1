h = int(input('hour: '))
m = int(input('min: '))
s = int(input('sec: '))

h %= 12
m %= 60
s %= 60

#за час стрелка проходит 30 градусов
gr = 360/12*h + 30/60*m + 30/3600*s
print('\ngr: ', gr)
