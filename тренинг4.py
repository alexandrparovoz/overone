# работа с массивом array

import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 12, 9])
print(np.concatenate((a, b))) # метод слияния массива а с б
print(a + b) # метод сложения массива а c б