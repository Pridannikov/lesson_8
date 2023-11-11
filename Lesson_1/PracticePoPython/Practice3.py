"""Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6
"""

# numbers = []
# for _ in range(int(input("Количество элементов: "))):
# numbers.append(int(input("Введите элемент: ")))

numbers = [2, 3, 2, 3, 1, 1, 5, 20, 20, 30]

# Вариант 1
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))


# Вариант 2
result = []
for num in numbers:
    if result.count(num) == 0:
        result.append(num)
print(len(result))

# Вариант 3 - Изменяем исходный список
for num in numbers[:]:
    while numbers.count(num) > 1:
        numbers.remove(num)
print(len(numbers))

"""Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
"""

numbers = [1, 2, 3, 4, 5]

k = 3
k = k % len(numbers) # Убираем лишнии итерации цикла


# Вариант [1] - Modified
list_result = []
len_list = len(numbers)
for i in range(len_list - k, len_list):
    list_result.append(numbers[i])
for i in range(len_list - k):
    list_result.append(numbers[i])
print(list_result)

# Вариант [2] Рабоьает с исходным кодом массива
for _ in range(k):
    numbers.insert(0, numbers.pop()) # удаляет последнее значение и добавляет его же в начало
print(numbers)

# Вариант [3] Замена по средством замены срезов
numbers = [1, 2, 3, 4, 5]
print(numbers[-k:] + numbers[:-k])



"""Напишите программу для печати всех уникальных значений в словаре."""

list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Вариант 1
"""Так делать плохо! Получаем ключ (key) в цикле (for key in dict_item)
а потом этот ключ (key) используем для получения значений словаря (dict_item[key])."""
unique_kyes = set()
for dict_item in list_1:
    for key in dict_item:
        unique_kyes.add(dict_item[key]) # Получаем значение по ключу и кладём в множество
print(unique_kyes)


# Вариант 1.1 - Modified
unique_kyes = set()
for dict_item in list_1:
    for value_dict in dict_item.values(): # Сразу получи значения словаря, а не его ключ
        unique_kyes.add(value_dict) # Кладём значение без обрашения по ключу (dict_item[key])
print(unique_kyes)

# Вариант 2
unique_kyes = set()
for dict_item in list_1:
    unique_kyes.update(dict_item.values())
print(unique_kyes)

"""Дан массив, состоящий из целых чисел. Напишите программу,
которая подсчитает количество элементов массива,
больших предыдущего (элемента с предыдущим номером)"""

numbers = [0, 1, 5, 2, 3]

# Вариант 1
count = 0
for i in range(len(numbers)): # Проходим циклом от 1, а не от 0
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)