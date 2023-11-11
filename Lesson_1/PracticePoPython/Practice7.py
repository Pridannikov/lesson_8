"""47. У вас есть код, который вы не можете менять
(так часто бывает, когда код в глубине программы
используется множество раз и вы не хотите ничего сломать):

transformation = <???>

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список

transormed_values = list(map(transformation, values))

Единственный способ вашего взаимодействия с этим кодом -
посредством задания функции transformation.

Однако вы поняли, что для вашей текущей задачи вам не нужно
никак преобразовывать список значений, а нужно получить его как есть.

Напишите такое лямбда-выражение transformation, чтобы transformed_values
получился копией values."""


# # Вариант 1
# def transformation(x):
#     return x


# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(transformation, values))
# print(transformed_values)
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# # Вариант 2
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


"""Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику."""

values = [0, 2, 9, 6, 4]

# Вариант 1
def same_by(characteristic, objects):
    for i in objects:
        if characteristic(i) != True: # Проверяем на совподение условия каждого объекта
            return False
    return True

# Вариант 2
def ame_by(characteristic, collection):
    return len(list(filter(characteristic, collection))) == 0

if same_by(lambda x: x < 10, values):
    print('same')
else:
    print('differen')




"""
У вас есть список словарей, каждый из которых представляет собой запись о продукте.
Вам нужно написать программу, которая спрашивает пользователя,
в каком порядке сортировать (по возрастанию или убыванию цены), и затем сортирует
список products по цене с использованием lambda-функции и выводит отсортированный список на экран.

"""

products = [
    {"name": "Шоколад", "price": [2.5, 5.0], "quantity": 100},
    {"name": "Молоко", "price": [1.0, 9.0], "quantity": 50},
    {"name": "Кофе", "price": [5.0, 12], "quantity": 30},
    {"name": "Чай", "price": [3.0, 15], "quantity": 80},
]


# Функция для сортировки списка словарей по цене
def sort_products(products, ascending: bool):
    return sorted(products, key=lambda x: x["price"][1], reverse=ascending)


def main():
# Ввод пользователя: "asc" для сортировки по возрастанию, "desc" - по убыванию
    sort_order = input("Введите порядок сортировки (asc/desc): ").strip().lower()

    if sort_order == "asc":
        sorted_products = sort_products(products, False)
    elif sort_order == "desc":
        sorted_products = sort_products(products, True)
    else:
        print("Неверный порядок сортировки.")
        return 0

    for product in sorted_products:
        print(product)


main()