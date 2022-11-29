if __name__ == '__main__':
    cake_rub = int(input('Введите цену пирожков в рублях: '))
    cake_pens = int(input('Введите цену ппирожков в копейках: '))
    cake_total = int(input('Введите число пирожков:'))
    sum_pens = (cake_total * cake_pens) % 100
    sum_rub = (cake_total * cake_rub) + (cake_total * cake_pens) // 100
    print('Пирожки стоят ', sum_rub, 'рублей и',sum_pens, 'копеек')
