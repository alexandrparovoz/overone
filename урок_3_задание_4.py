# определить попадет ли шахматный слон в заданную клету

if __name__ == '__main__':
    a1 = int(input('Введите номер стлбца:'))
    b1 = int(input('Введите номер строки:'))
    a2 = int(input('Введите номер стлбца:'))
    b2 = int(input('Введите номер строки:'))
    if a1 - a2 == b1 - b2:
        print('Yes')
    elif a1 + b1 == a2 + b2:
        print('Yes')
    else:
        print('No')