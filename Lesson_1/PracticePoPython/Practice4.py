"""25. Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"""

# stroka = 'a a a b c a a d c d d'
# stroka = stroka.split()
# count = {}
# for i in stroka:
#     if i in count:
#         print(f"{i}_{count[i]}", end=" ")
#     else:
#         print(f"{i}", end=" ")
#     count[i] = count.get(i, 0) +1

"==========================================================="
"""Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте."""

# Вариант 1
text = """She sells sea shells on the sea
shore The shells that she sells are sea
shells I'm sure So if she sells sea shells
on the sea shore I'm sure that the shells are sea shore shells"""
# text = text.split() # Создание списка по словам
# unique_words = set()
# for word in text:
#     unique_words.add(word.lower())
# print(len(unique_words))


# Вариант 2
text = """She sells sea shells on the sea
shore The shells that she sells are sea
shells I'm sure.So if she sells sea shells
on the sea shore I'm sure that the shells are sea shore shells"""

# print(len(set(text.lower().split())))

"""----------------------------------------------
Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)"""
n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)


