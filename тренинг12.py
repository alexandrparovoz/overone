# сортирjвка вставками

def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i
        while j > 0 and arr[j - 1] > x: # если j больше ноля и элемент[j - 1] больше элемента х
            arr[j - 1], arr[j] = arr[j], arr[j - 1] # то меняем местами элементы [j - 1] и [j]
            j -= 1  # теперь сверяем в цикле while элемент смещенный правее на единицу
        arr[j] = x  # не эабываем поставить элемент х в то положение на котором остановился j
    return arr

if __name__ == '__main__':
    li = [33, 3, 1, 88, 33, 21, 9, -9]
    print(insert_sort(li))