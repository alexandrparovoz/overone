if __name__ == '__main__':

    number = 55
    running = True

    while running:
        guess = int(input('Bring integer: '))

        if guess == number:
            print('Grate, you are win!')
            running = False  #  это останавливает цикл while
        elif guess < number:
            print('No, guess number some more then your number')
        else:
            print('No, guess number some less then your number')

    else:
        print('Cycle while finished')  # Я не понял смысл применения этого предложения
    print('Closed')