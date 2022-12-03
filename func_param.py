if __name__ == '__main__':

    def printMax(a, b):
        if a > b:
            print(a, 'more than', b)
        elif a == b:
            print(a, 'equals', b)
        else:
            print(b, 'more than', a)
    printMax(3, 8)  #  прямая передача значений

    x = 7
    y = 3

printMax(x, y)  # передача переменных в качестве аргумнтов