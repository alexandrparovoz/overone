# яша в бассейне

if __name__ =='__main__':
    n = int(input('Введите длину:'))
    m = int(input('Введите ширину:'))
    x = int(input('Расстояние до длинного бортика:'))
    y = int(input('Расстояние до короткого бортика:'))
    m_half = m / 2

    if y < x and x < m_half:
        print('Плыви на расстояние ', y, ' метров ')
    elif y < m - x and x > m_half:
        print('Плыви на расстояние ', y, ' метров ')
    elif y > n - m_half and x < m_half and n - y <  x:
        print('Плыви на расстояние ', n - y, ' метров ')
    elif y > n - m_half and x > m_half and (y - (n - m_half)) < (m - x):
        print('Плыви на расстояние ', n - y, ' метров ')
    elif y > m - x and x > m_half:
        print('Плыви на расстояние ', m - x, ' метров ')
    else:
        print('Плыви на расстояние ', x, ' метров ')

