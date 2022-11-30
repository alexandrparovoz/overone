if __name__ == '__main__':

    n = int(input('Ввести координаты n:'))
    m = int(input('Ввести координаты m:'))
    x = int(input('Ввести короткие  координаты x:'))
    y = int(input('Ввести длинные  координаты y:'))

    if n > m:
        temp = n
        n = m
        m = temp
    if x > n / 2:
        x = n - x
    if y > m / 2:
        y = m - y
    if x < y:
        print(x)
    else:
        print(y)


