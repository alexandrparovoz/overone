# попадет ли шахматный король на заданнуюклетку за один ход

if __name__ == '__main__':
    a1 = int(input('Введите номер столбца:'))
    b1 = int(input('Введите номер строки:'))
    a2 = int(input('Введите номер столбца:'))
    b2 = int(input('Введите номер строки:'))

    if (a1 + 1) == a2 and ((b1 + 1) == b2 or (b1 - 1) == b2 or (b1 == b2)):
        print('Yes')
    elif (a1 - 1) == a2 and ((b1 + 1) == b2 or (b1 - 1) == b2 or (b1 == b2)):
        print('Yes')
    elif a1 == a2 and ((b1 - 1) == b2 or (b1 + 1) == b2):
        print('Yes')
    else:
        print('No')
