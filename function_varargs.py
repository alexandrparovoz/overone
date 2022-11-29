# показывам переменное число параметров

def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:  # проходим по всем элементам КОРТЕЖА
        print('single_item',single_item)
    for first_part, second_part in phonebook.items():  # проходим по всем элментам  СЛВАРЯ
        print(first_part, second_part)

total(10, 1, 2, 3, 33, Jack=1123, John=2231, ufo=887755, Inge=1560) 