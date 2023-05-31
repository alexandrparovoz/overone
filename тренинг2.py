# работа  со словарем
# сортировка по ключу методом sorted()

dc = {'6': 'glory', '4': 'wrong', '2': 'beauty','7': 'usially'}
dc.items() # разбивает словарь на кортежи (ключ, значение)
#  метод sorted() в необяз параметре key (по которому идет сортировка) принимает функцию, а та параметр х(кортеж)
sorted_dict = sorted(dc.items(), key=lambda x: x[0]) #  и идет сортировка по первому индексу( а это ключ)
                                                     #  а если x[1] то по значению
print(sorted_dict)

# получение СПИСКА ключей из словаря (отсортированного)

li = sorted(list(dc))
print(li)

# генерация словаря  из списка с методом enumerate
s = ['w', 'f', 'k', 'm']
d = {key1 : value1 for  key1, value1 in enumerate(s)}
print(d)

# есть два массива. создаем слварь
# первый массив - ключи, второй - значения

a = [12, 11, 32]
b = ['d', 'x', 'w']
dict1 = dict(zip(a, b))
c = dict(zip(a, range(3))) # генерация словаря с поощью zip i range
print(c)
print(f'new dictionary -  {dict1}')