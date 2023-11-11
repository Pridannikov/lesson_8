# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))


"""def fact(n):
    return 1 if n == 1 else n * fact(n-1) # рекурсия (ест операционную память при работе)
print(fact(6))"""

"""Последовательностью Фибоначчи называется последовательность
чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""
# a b
# 0, |1, 1|, 2, 3, 5, 8...
# -----------------
# Решение с использованием for
def fib_for(n):
    a, b = 0, 1
    for _ in range(n): # _ - так как переменная не используется
        a, b = b, a + b # Обмен значениями
    return a

print(fib_for(5))

# -----------------
# Решение через рекурсию
def fib_2(n):
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)


def fib_2(n):
    return n if n <= 1 else fib_2(n - 1) + fib_2(n - 2)

''' Решение задачки на подмену оценок'''
# spisok = [2, 5, 3, 3, 3, 1, 1, 4]
# mx = 0
# mn = 6
# for e1 in spisok:
#     if e1 > mx:
#         mx = e1
#     if e1 < mn:
#         mn = e1
# # for i in range(len(spisok)):
# #     if spisok[i] == mn:
# #         spisok[i] = mx
# # print(*spisok)
# print([mx if spisok[i] == mn else spisok[i] for i in range(len(spisok))]) # тернарный оператор 
# print([mx if spisok[i] == mn else spisok[i] 
#        for i in range(len(spisok)) if mx >= 4 and spisok[i] >= 4]) # тернарный оператор 

''' Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3'''

# def rever(n):
#     if n == 0:
#         return ""
#     num = input()
#     return rever(n - 1) + " " + num

# print(rever(3))

"""Даны два целых числа A и В.
Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания, если A > B"""

def numbers(a, b):
    if a == b:
        return b 
    if a < b:
        return f"{a} {numbers(a + 1, b)}"
    if a > b:
        return f"{a} {numbers(a - 1, b)}"
print(numbers(1, 10))
print(numbers(10, 1))