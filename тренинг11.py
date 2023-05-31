# многое о list comprehension - генераторе списков

li1 = [x for x in range(5)] # ггнерируем прссто список
print('Li1 -', li1)
li2 = [[x for x in range(6)] for y in range(3)] # генер список списков
print('Li2 - ', li2)

l = [3, 1, 6, 2, 9, 33, 2]
odd_li = [i for i in l if i % 2] # генер новый список выбирая нечетные
print('Odd_li -', odd_li)

# интересно - есть список словарей, надо создать список значений конкретных ключей
people = [
    {
    1: 'one',
    11: 'eleven',
    'city': 'Minsk'},
    {
    2: 'two',
    22: 'twety two',
    'city': 'Moscow'},
    {
    3: 'three',
    33: 'thirdty three',
    'city': 'Tallinn'}]

# генерируя список мы сначала вынимаем каждый словарь(person[keys])
#  а потом из словаря достаем значение по конкретному ключу
cities = [person[keys] for person in people for keys in person if keys == 'city']
print('Cities is -',cities)