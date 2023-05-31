# как передается переменная (по ссылке или значению)
name = 'graff'

def func(str1):
    print(id(str1))
    print(id(name))

func(name)

# s = 'qwerty'
# print(s[::-1])
# li = ['1', '2', '3']
# li.reverse()
# print(li)

li3 = [['a'], ['b'], ['w']]
li4 =list(li3)
li3[2].append('g')
print(li4)
print(li3)

