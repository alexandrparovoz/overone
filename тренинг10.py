# есть словарь, найти два ключа с наибольшими значениями

a = {'a': 200, 'b': 210, 'c': 199, 'd': 300, 'e': 102}
b = sorted(a.values())
for key, value in a.items():
    if value in b[-2:]:
        print(key, end="")
print('\n', b)
print(b[-2:])