import math
r = float(input("Введите внутренний радиус кольца: "))
R = float(input("Введите внешний радиус кольца: "))

S = math.pi * pow(R, 2) - math.pi * pow(r, 2)
print("Площадь кольца: ", S)
