# билеты в зоопарк дети до 2-х лет -бесплатно
# с 3х до 12 - 14$ , с  66 - 18$ , остальные - 23$


age_of_each = int(input('введите возраст члена группы:  '))
count_0_2 = 0
count_of_3_12 = 0
count_of_13_65 = 0
count_of_66 = 0
while age_of_each != '':
    if age_of_each <= 2:
        count_0_2 = count_0_2 + 0
    if (age_of_each >= 3) and (age_of_each <= 12):
        count_of_3_12 = count_of_3_12 + 14
    if (age_of_each >= 13) and (age_of_each <= 65):
        count_of_13_65 = count_of_13_65 + 23
    if age_of_each > 65:
        count_of_66 = count_of_66 + 18
    second_each = int(input('введите возраст следующего'))
    print(count_0_2 + count_of_3_12 + count_of_13_65 + count_of_66)