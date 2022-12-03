if __name__ == '__main__':

# применяем глобальную переменную  GLOBAL

    x = 50

    def func():
        global x

        print(' x equals', x)
        x = 2
        print(' Замеям глобальное значение х на', x)

    func()
    print('Значение х составляет', x)