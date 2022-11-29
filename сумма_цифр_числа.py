if __name__ == '__main__':
    number = int(input('Введите  чтырехзачное число:'))
    a = number % 10
    b = number % 100 // 10
    c = number % 1000 // 100
    d = number // 1000
    result = a + b + c + d
    print('Сумма всех цифр числа равна:', result)

