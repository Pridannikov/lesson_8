from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
            print('Данные успешно запианны.')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')
            print('Данные успешно запианны.')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines() # .readlines читает все строки в файле
        print(*data_second)
    return data_first, data_second


def edit_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))
    while number_file != 1 and number_file != 2:
        print('Друг, нет такого файла. Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1: # Можно сделать нумерацию внутри файла    
        print("Какую именно запись по счету Вы хотите изменить?")
        print(*(f"{i} {line.rstrip()}" for i, line in enumerate(data_first, 1)), sep = '\n')                
        number_journal = int(input('Введите номер записи: ')) - 1 
               
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        
        data_first_num = data_first[number_journal]        
        data_first[number_journal] = (f'{name}\n{surname}\n{phone}\n{address}\n\n')
                  
        print(f"\nЗапись: {data_first_num} Заменена на: {name};{surname};{phone};{address}")

        data_first = [x.lstrip("\n") for x in data_first]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        print(*(f"{i} {line.rstrip()}" for i, line in enumerate(data_second, 1)), sep = '\n')
        number_journal = int(input('Введите номер записи: ')) -1
       
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        
        data_second_num = data_second[number_journal]        
        data_second[number_journal] = (f'{name};{surname};{phone};{address}\n\n')

        print(f"\nЗапись: {data_second_num} Заменена на: {name};{surname};{phone};{address}")
        data_second = [x.strip("\n") for x in data_second]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write('\n'.join(data_second))



def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Друг, нет такого файла. Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1: # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        print(*(f"{i} {line.rstrip()}" for i, line in enumerate(data_first, 1)), sep = '\n')
        number_journal = int(input('Введите номер записи: ')) - 1
        data_first_num = data_first[number_journal]        
        data_first.pop(number_journal)            
        print(f"Удалена запись: {data_first_num}\n")
        data_first = [x.lstrip("\n") for x in data_first]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        print(*(f"{i} {line.rstrip()}" for i, line in enumerate(data_second, 1)), sep = '')
        number_journal = int(input('Введите номер записи: ')) -1
        data_second_num = data_second[number_journal]
        data_second.pop(number_journal + 1)         
        data_second.pop(number_journal)  
        print(f"Удалена запись: {data_second_num}\n")
        data_second = [x.strip("\n") for x in data_second]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write('\n'.join(data_second))


        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
