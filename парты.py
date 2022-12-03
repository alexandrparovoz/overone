if __name__ == '__main__':

    class_1 = int(input('Введите число учениов 1 класса:' ))
    class_2 = int(input('Введите число учениов 2 класса:' ))
    class_3 = int(input('Введите число учениов 3 класса:' ))
    part1 = class_1 // 2 + class_1 % 2
    part2 = class_2 // 2 + class_2 % 2
    part3 = class_3 // 2 + class_3 % 2
    total = part1 + part2 + part3
    print(total)