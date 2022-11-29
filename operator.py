if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())
    if a > b:
        num = a
        a = b
        b = num
    if b > c:
        num = b
        b = c
        c = num
    if a > b:
        num = a
        a = b
        b = num
    print(a, b, c)
