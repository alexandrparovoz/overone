# снова работа со словарями

dict1 = {1: 'one', 4: 'four', 8: 'eighth'}
dict2 = {3: 'three', 7: 'seven', 5: 'five'}

# три способа объединения словарей
dict3 = (dict1, dict2) # два разных словаря в третьем
print('Dict3 -',dict3)

dict1.update(dict2) # присоединение второго к первому
print('"Dic1 + dict2 - "',dict1)

dict4 = {**dict1, ** dict2} # объединение двух в третьем
print('Dict4 - ', dict4)

dict5 = dict1 | dict2  # объединение двух в третьем (для питон 3.9 и выше)
print('Dict5 - ', dict5)