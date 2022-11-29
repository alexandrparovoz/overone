# вывести в секундах разницу во времени между двумя моментами
if __name__ == '__main__':


    hour1 = int(input('Введите час1:  '))
    minute1 = int(input('Введите минуты1; '))
    seconds1 = int(input('Bведите секунды1; '))

    hour2 = int(input('Введите час2:  '))
    minute2 = int(input('Введите минуты2: '))
    seconds2 = int(input('Bведите секунды2: '))

    sum_hour = (hour2 - hour1) * 3600
    sum_minute = (minute2 - minute1) * 60
    sum_seconds = seconds2 - seconds1

    result = sum_hour + sum_minute + sum_seconds
    print(result)