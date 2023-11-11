"""9. По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while"""

# n = int(input("Введите число: "))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1

# print(fact, i)

"""Дано натуральное число A > 1. Определите, каким по счету числом
Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1."""

# A = 8 -> 7
# A = 10 -> -1
# A = 13 -> 8

# 1, 2, 3, 4, 5, 6, 7, 8 -- Index
# |0, 1|, 1, 2, 3, 5, 8, 13, 21 -- Fib Numbers

"""# Вариант 1
A = int(input('A = '))
a1 = 0
a2 = 1
next_a = 0
i = 2
while next_a < A:
    next_a = a1 + a2 
    a1 = a2
    a2 = next_a
    i += 1
    if next_a > A:
        i = -1
print(i)"""

"""# Вариант 2 
A = int(input('A = '))
a1, a2 = 0, 1
i = 2
while a2 < A:
    a1, a2 = a2, a1 + a2
    i +=1
    if a2 > A:
        i = -1
print(i)"""




"""n = int(input("Сколько дней: "))
count = 0
global1_max = 0
for i in range(n):
    x = int(input("Градусы: "))
    if x > 0:
        count += 1
    else:
        if global1_max < count:
            global1_max = count
            count = 0
if global1_max < count:
    global1_max = count
print(global1_max)"""

"""15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
"""

"""N = int(input('Ко-во арбузов: '))
min = float('inf') #Объявляем бесконечностью
max = float('-inf') #Объявляем бесконечностью

# min = 100
# max = 0


for _ in range(N):
    x = int(input('Вес арбуза: '))
    if x > max:
        max = x
    if x < min:
        min = x

print(f'Т - {min}, И - {max}')"""


# Задача про монетки
# # n = int(input("Сколько монет: "))
# coins = [0, 0, 0, 0, 0, 0, 0]
# count1 = 0
# count2 = 0
# global1_max = 0
# for i in list(coins):
#     if i == 1:
#         count1 += 1
#     else:
#         count2 += 1
# if count2 > count1:
#     global1_max = count1
# else:
#      global1_max = count2

# print(global1_max)

# Задача про Катю и Петю

# x = 12
# y = 27
# sx = 0
# sy = 0
# i = 0
# while i != y:
#     sy +=1
#     sx = (x - sy)
#     i = (sx * sy)
# if sx == sy:
#     print(f"{sx} {sy}")
# else: 
#     print(f"{sy} {sx}")
#     print(f"{sx} {sy}")

"""Требуется вывести все целые 
степени двойки (т.е. числа вида 2k), 
не превосходящие числаN"""

n = 3
p = 1
while p <= n:
    print(p,end = '\n')
    p = p*2