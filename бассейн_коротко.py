if __name__ == '__main__':

    n = int(input('ВВести координаты n:'))
    m = int(input('ВВести координаты m:'))
    x = int(input('ВВести корткие  координаты x2:'))
    y = int(input('ВВести длинные  координаты y2:'))

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


