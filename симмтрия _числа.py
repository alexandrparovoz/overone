# проверить симметрично ли четырехзначное число разделенное надвое
num = int(input('Введите четырехзначное число: '))
half_of_num1 = num // 100
half_of_num2 = num % 100
result = (half_of_num1 - half_of_num2) + 1
print(result)

