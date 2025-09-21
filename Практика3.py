# Если на улице дождь (if), то возьми зонт.
# Иначе, если солнце (elif), то надень солнечные очки.
# Во всех остальных случаях (else), просто выходи из дома.

# В программировании это работает абсолютно так же.
# Ветвление — это инструмент, который позволяет программе делать выбор
# и выполнять разные участки кода в зависимости от того, является ли
# какое-то условие истинным (True) или ложным (False).


# 1. Базовые конструкции
'''age = int(input("Сколько вам лет? "))
# if age >= 18: Если условие age >= 18 - Правда
    print("Добро пожаловать!") # Выполнится только эта строка
print("Программа завершена.") # Это строка выполнится всегда'''


# 2. if - else (если - иначе)
'''age = int(input("Сколько вам лет? "))
if age >= 18:
    print("Добро пожаловать!")
else:
    print("Доступ запрещён!")
print("Программа завершена.")'''


# 3. if - elif - else (если - иначе если - иначе)
'''grade = int(input("Ваша оценка: "))
if grade == 5:
    print("Отлично!")
elif grade == 4:
    print("Хорошо!")
elif grade == 3:
    print("Удовлетворительно!")
elif grade == 2:
    print("Плохо!")
else:
    print("Такой оценки не существует!") # Сработает для 1, 6, 100 и т.д'''


# Сам. Работа
# 1.1
'''a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

print("Числа, принадлежащие интервалу [1, 3]:")
if 1 <= a <= 3:
    print(a)
if 1 <= b <= 3:
    print(b)
if 1 <= c <= 3:
    print(c)'''


# 1.2
print("Программа выведет состоит ли двузначное число из одинковых цифр")
n = int(input("Введите двузначное число: "))

# if n == 11 or n == 22 or n == 33 or n == 44 or n == 55 or n == 66 or n == 77 or n == 88 or n == 99:
#     print("ДА!")
# else:
#     print("Нет!")

# или 
digit1 = n // 10
digit2 = n % 10

if digit1 == digit2:
    print("ДА!")
else:
    print("Нет!")


# 2.1
print("Задание 2.1")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b:
    x = a+b
elif a > b:
    x = a-b
else: # Сработает только если a == b
    x = 1 or a == b

print(x)


# 2.2
print("Задание 2.2")
f = int(input("num1: "))
k = int(input("num2: "))

if f < 5 or k > 2:
    R = f + k - 1
elif k < 2:
    R = k**2
else:
    R = 1 or k == 2

print(R)


# 2.3
print("Задание 2.3")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b:
    C = a + b
elif a > b or a > 3:
    C = b**2 - b
else:
    C = b**2 - 1

print(C)


# 2.4
print("Задание 2.4")
v = int(input("num1: "))
k = int(input("num2: "))

if v < k:
    Z = v - k + 1
elif k > v:
    Z = k**2 - v**2
else:
    Z = k**2 - k

print(Z)


# 2.5
print("Задание 2.5")

f = int(input("num1: "))
z = int(input("num2: "))

if f < 5:
    z = f + 2
elif f > 5:
    z = f - 1
else:
    z = 1
print(z)


# 2.6
print("Задание 2.6")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b and b > 4:
    x = a+b
    if a > b:
        x = a - b
else:
    x = a**2

print(x)


# 2.7
print("Задание 2.7")
v = int(input("num1: "))
k = int(input("num2: "))

if v < 2 and k == 1:
    B = v - k + 1
    if k > v:
        B = k**2 + v**2
else:
    B = k**2 + v

print(B)


# 2.8
print("Задание 2.8")
x = int(input("num1: "))
y = int(input("num2: "))

if x < 2 and y == 2:
    B = x * y
    if x > y:
        B = y**2 + x**2
else:
    B = x**2 + 2
print(B)


# 2.9
print("Задание 2.9")
f = int(input("num1: "))
v = int(input("num2: "))
k = int(input("num3: "))

if f < 4 and v > 6:
    S = f + v
elif v < 6:
    S = k ** 2
else:
    S = 2 * v
print(S)

# 2.10
print("Задание 2.10")
k = int(input("num1: "))
c = int(input("num2: "))

if k < 5 and c > 4:
    X = k + c ** 2
elif k > c and k > 3:
    X = c ** 2 + 2
else:
    X = c - 1
print(X)

# 2.11
print("Задание 2.11")
x = int(input("num1: "))
y = int(input("num2: "))

if x == 4 and y < 2:
    q = x + x * y
elif x < y:
    q = y ** 2 + 1
else:
    q = y ** 2 + 4
print(q)

# 2.12
print("Задание 2.12")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b:
    R = a - b + 1
elif a > b and a > 3:
    R = b ** 2 - b
else:
    R = b ** 2 - 1
print(R)

# 2.13
print("Задание 2.13")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b:
    x = 2 * a + 2 * b
elif a > b:
    x = a - b + 1
else:
    x = b ** 2 - b
print(x)

# 2.14
print("Задание 2.14")
f = int(input("num1: "))
k = int(input("num2: "))

if f < k:
    R = f + k ** 2 - 1
elif k < 2 and f == 3:
    R = k ** 2
else:
    R = f - 1
print(R)

# 2.15
print("Задание 2.15")
a = int(input("num1: "))
b = int(input("num2: "))

if a < 2 and b > 3:
    C = a + b ** 2
elif a > b and a > 3:
    C = b ** 2 + 2
else:
    C = b
print(C)


# Задача 3
print("Задание 3.1")
a = int(input('num1 = '))
b = int(input('num2 = '))
if a > b:
   print(a,'наибольшее')
else:
   print(b,'наибольшее')

print("Задание 3.2")
a = int(input('num = '))
if a % 2 == 0:
   print(a,' четное')
else:
   print(a,' нечетное')

print("Задание 3.3")
a = int(input('num = '))
if a % 2 == 0:
   print(a,'четное')
else:
   print(a,'нечетное')