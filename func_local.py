x = 55

def func(x):
    print('x equals', x)
    x = 2
    print("Замена локального х на", x)

func(x)
print('x still ', x)
