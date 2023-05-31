# удаление всех пробелов из строки два способа

a = 'weenj qqq hbhb hbbb'
b = ''.join(a.split()) # сначала слит разобьет строку на части и сдлает список
                       # а джоин соединит этот список в сртоку без пробелов
print(b)

# второй способ

s = 'ooo nnn www'
print(s.replace(' ', ''))  # НО сам объкт не изменяется


# ТЕРНАЛЬНЫЙ ОПЕРАТОР ( в одну строку)
x = 5
y = 10
print('more' if x > 6 else 'less')

# работа сплита и джоинта наглядно
s = 'eryuW ncvvmmcW loW qqqW'
b = s.split()
print(b)
a = ' -- '.join(b)
print(a)