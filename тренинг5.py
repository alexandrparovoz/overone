# методы удаления из списка дубликатов

li = [2, 3, 1, 2, 4, 3, 8]
li_2 = list(set(li)) # преобразование во множество и обратно в лист
print(li_2)
li_3 = []
for i in li:
    if i not in li_3:
        li_3.append(i)
print(li_3)

#  объединение двух списков в список кортежей

ls_1 = ['a', 'b', 'c']
ls_2 = ['1', '2', '3']
tp1 = tuple(ls_1)
tp2 = tuple(ls_2)
#tp3 = tp1 + tp2
#tp4 = list((tp1 + tp2))
ls = [tp1, tp2]
print(ls)

# или через zip но вывод другой - попарный

ls_1 = ['a', 'b', 'c', 'd', 'e'] # лишний элемент не виден
ls_2 = ['1', '2', '3', '4']
tp = [(k, v) for k, v in zip(ls_1, ls_2)]
print(tp)