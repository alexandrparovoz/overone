if __name__ == '__main__':

#  только ключевые параметры

    def total(initial=5, *numbers, extra_number):
        count = initial
        for number in numbers:
            count += number
        count += extra_number
        print(count)

    total(10, 1, 2, 3, extra_number=50)
# если не назначить  extra_number то выдаст ошибку