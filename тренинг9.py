# метод сортировки пузырьком
# сначала рандомно создаем список

import random

a = []
n = 10
i = 0
while i < n:
    a.append(random.randint(1,100))
    i += 1
print('Non sorted list - ', a)

# далее метод пузырьком

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print('Sorted list - ', a)
