from functools import reduce
# показывам работу метода reduce
def func(x, y):
    return x + y

li = [77, 333,65]
a = reduce(func, li)
print(a)
