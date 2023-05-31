if __name__ == '__main__':

    number = 23
    guess = int(input('введите целое число: '))

    if guess == number:
        print('Perfect, you are win!')
        print('But you are have not any prize')
    elif guess < number:
        print('No, guess number same more, then your number')
    else:
        print('No, guess number same less then your number')
    print('Finished!')  #  Это выражение ыполняется после исполнения оператора if
