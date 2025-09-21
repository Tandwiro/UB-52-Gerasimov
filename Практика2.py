# math.ceil(x) - Возвращает ближайшее целое число большее, чем x
# math.fabs(x) - Возвращает абсолютное значение числа x
# math.factorial(x) - Вычисляет факториал x
# math.floor(x) - Возвращает ближайшее целое число меньшее, чем x
# math.exp(x) - Вычисляет e**x
# math.log2(x) - Логарифм по основанию 2
# math.log10(x) - Логарифм по основанию 10
# math.log(x[,base]) - По умолчанию вычисляет логарифм по основанию e,дополнительно можно указать основание логарифма
# math.pow(x, y) - Вычисляет значение x в степени y
# math.sqrt(x) - Корень квадратный от x

# Пример применения вышеописанных функций над числами
'''import math
a = 10
b = -5
c = 4.3
d = 3
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
z = math.ceil(a)
print('math.ceil(',c,') = ', z)
z = math.fabs(b)
print('math.fabs(',b,') = ', z)
z = math.factorial(a)
print('math.factorial(',a,') = ', z)
z = math.floor(c)
print('math.floor(',c,') = ', z)
z = math.exp(b)
print('math.exp(',b,') = ', z)
z = math.log2(a)
print('math.log2(',a,') = ', z)
z = math.log10(a)
print('math.log10(',a,') = ', z)
z = math.log(d, a)
print('math.log(',d,' , ',a,') = ', z)
z = math.pow(a, d)
print('math.pow(',a,' , ',d,') = ', z)
z = math.sqrt(a)
print('math.sqrt(',a,') = ', z)'''


# math.cos(x) - Возвращает cos числа X
# math.sin(x) - Возвращает sin числа X
# math.tan(x) - Возвращает tan числа X
# math.acos(x) - Возвращает acos числа X
# math.asin(x) - Возвращает asin числа X
# math.atan(x) - Возвращает atan числа X

# Пример применения вышеописанных функций над числами
'''import math
x = 1
print('x = ', x)

z = math.cos(x)
print('math.cos(',x,') = ', z)

z = math.sin(x)
print('math.sin(',x,') = ', z)

z = math.tan(x)
print('math.tan(',x,') = ', z)

z = math.tan(x)
print('math.tan(',x,') = ', z)

z = math.acos(x)
print('math.acos(',x,') = ', z)

z = math.asin(x)
print('math.asin(',x,') = ', z)

z = math.atan(x)
print('math.atan(',x,') = ', z)'''


# Константы:
# math.pi - число Pi.
# math.e - число е (экспонента).

# Пример
# Напишите программу, которая бы вычисляла заданное арифметическое
# выражение при заданных переменных. Ввод переменных осуществляется с
# клавиатуры. Вывести результат с 2-мя знаками после запятой.

# import math
#
# x = int(input('Enter a number: '))
# print('x = ', x)
# t = int(input('Enter a number: '))
# print('t = ', t)
#
# a = (9 * math.pi*t + 10 * math.cos(x))
# b = (math.sqrt(t) - math.fabs(math.sin(t)))
# c = math.pow(math.e, x)
#
# z = (a / b) * c
# print("z = {0:2f}".format(z))


import math

# Задание 1
print("Задание 1")
x = 14.26
y = -1.22
z = 3.5*10**(-2)

a = ( 2 * math.cos(x - 2/3) )
b = ( 1/2 + (math.pow(math.sin(y),2)))
c = 1 + (z**2) / (3 - z**2/5)

s1 = ((a / b) * c)
print(f"s = {s1:.6f}")
print("--------------")


# Задание 2
print("Задание 2")

x = -4.5
y = 0.75*10**(-4)
z = -0.845*10**2

s2 = (math.sqrt(9 + (x-y)**2)**(1/3) / (x**2 + y**2 + 2)) - math.exp(abs(x-y)) * (math.tan(z))**3
print(f"s = {s2:.5f}")
print("--------------")


# Задание 3
print("Задание 3")
x = 3.74 * 10 ** -2
y = -0.875
z = -0.16 * 10 ** 2

a = 1 + (math.sin(x + y))**2
b = x - (2*y) / (1 + x**2 * y**2)
znam = 2 + math.fabs(b)
c = (math.cos(math.atan(1 / z)))**2

s3 = a / znam + c
print(f"s = {s3:.5f}")
print("--------------")


# Задание 4
print("Задание 4")
x = 0.4 * 10 ** 4
y = -0.875
z = -0.475 * 10 ** -3

a = (math.cos(x) - math.cos(y))
znam = math.fabs(a) ** (1+2*(math.sin(y))**2)
b = (1 + z + (z**2 / 2) + (z**3 / 3) + (z**4 / 4))

s4 = znam * b
print(f"s = {s4:.5f}")
print("--------------")


# Задание 5
print("Задание 5")

x = -15.246
y = 4.642 * 10 ** -2
z = 21

a = math.log(y ** (math.sqrt(-x)))
znam = math.fabs(a)*(x-y/2)
b = math.sin(math.atan(z))**2

s5 = znam * b
print(f"s = {s5:.3f}")
print("--------------")


# Задание 6
print("Задание 6")
x = 16.55*10**-3
y = -2.75
z = 0.15

p1 = math.sqrt(x) + x ** (y + 2)
part1 = 10 * p1
sqrt = math.sqrt(part1)

part2 = math.asin(z) ** 2
znam = math.fabs(x-y)
part = part2 - znam

s6 = sqrt * part
print(f"s = {s6:.4f}")
print("--------------")


# Задание 7
print("Задание 7")
x = 0.1722
y = 6.33
z = 3.25 * 10**-4

part1 = 5 * math.atan(x)
part2 = (1/4) * math.acos(x)
num = x + 3 * math.fabs(x-y) + x**2 # нумиратор
denom = math.fabs(x-y) * z + x**2 # деномиратор
frac = num / denom

s7 = part1 - part2 * frac
print(f"s = {s7:.3f}")
print("--------------")


# Задание 8
print("Задание 8")

x = -2.235*10**-2
y = 2.23
z = 15.221

znam = math.exp(math.fabs(x-y))
part1 = znam * (math.fabs(x-y))**(x+y)
part2 = math.atan(x) + math.atan(z)
part1_2 = part1 / part2
part3 = (x**6 + math.log(y)**2) ** (1/3)

s8 = part1_2 + part3
print(f"s = {s8:.4f}")
print("--------------")


# Задание 9
print("Задание 9")

x = 1.825*10**2
y = 18.225
z = -3.298*10**-2

part = x**(y/x) - (y / x)**(1/3)
part1 = math.fabs(part)

num = y - x
denom = 1 + (y - x)**2
frac = num / denom
part2 = frac * math.cos(y)

part3 = - (z / (y-x))

s9 = part1 + part2 + part3
print(f"s = {s9:.5f}")
print("--------------")


# Задание 10
print("Задание 10")

x = 3.981*10**-2
y = -1.625*10**3
z = 0.512

part1 = 2 ** (-x)
sqrt_y = (math.sqrt(math.fabs(y))**(1/4))
sqrt_e = (math.sqrt(math.exp( (x-1) / (math.sin(z) ))) ) ** (1/3)
part2 = math.sqrt(x + sqrt_y)

s10 = part1 * part2 * sqrt_e
print(f"s = {s10:.5f}")
print("--------------")


# Задание 11
print("Задание 11")

x = 6.251
y = 0.827
z = 25.001

fabs_x = (math.fabs(x)) ** (1/3)
part_1 = y ** fabs_x

part_2 = math.cos(y) ** 3

fabs_xy = math.fabs(x - y)
sinus = math.sin(z) ** 2
sqrt_xy = math.sqrt(x + y)
num = fabs_xy * (1 + sinus / sqrt_xy)

denom = math.exp(fabs_xy) + x / 2

frac = num / denom

s11 = part_1 + part_2 * frac
print(f"s = {s11:.6f}")
print("--------------")


# Задание 12
print("Задание 12")

x = 3.251
y = 0.325
z = 0.466*10**-4

part_1 = 2 ** (y ** x)
part_2 = (3 ** x) ** y
num = y * math.atan(z) - (1/3)
denom = math.fabs(x) + 1 / (y**2 + 1)
frac = num / denom

s12 = part_1 + part_2 - frac
print(f"s = {s12:.5f}")
print("--------------")


# Задание 13
print("Задание 13")

x = 17.421
y = 10.365*10**-3
z = 0.828*10**5

sqrt1 = (x - 1) ** (1/3)
sqrt2 = y + sqrt1
part_1 = sqrt2 ** (1/4)

fabs_xy = math.fabs(x - y)
sin = math.sin(z) ** 2
tan = math.tan(z)
part_2 = fabs_xy * (sin + tan)


s13 = part_1 / part_2
print(f"s = {s13:.6f}")
print("--------------")


# Задание 14
print("Задание 14")

x = 12.3 * 10**-1
y = 15.4
z = 0.252*10**3

part_1 = y ** (x+1)
fabs_xy = (math.fabs(y - 2) + 3)
part_2 = math.sqrt(fabs_xy) ** (1/3)

part_3 = x + (y / 2)
part_4 = 2 * (math.fabs(x + y))

sin = -1 / math.sin(z)
part_5 = (x + 1) ** sin

s14 = part_1 / part_2 + part_3 / part_4 * part_5
print(f"s = {s14:.4f}")
print("--------------")


# Задание 15
print("Задание 15")
x = 2.444
y = 0.869*10**-2
z = -0.13*10**3

num = x ** (y + 1) + math.exp(y - 1)
denom = 1 + x * math.fabs(y - math.tan(z))
part_1 = num / denom

part_2 = 1 + math.fabs(y - x)
temp = part_1 * part_2

term = (math.fabs(y - x) ** 2) / 2

fram = - (math.fabs(y - x) ** 3) / 3

s15 = temp + term + fram
print(f"s = {s15:.5f}")