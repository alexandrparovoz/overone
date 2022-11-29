# объявляем одной из переменных значение по умолчанию

def say(message, times=1):
    print(message * times)


say('Hello!')
say('World', 4)