# вариант 1
def my_func(x=int(input('введите действительное положительное число ')),
            y=int(input('введие целое отрицательное число '))):
    print(x ** y)


my_func()


# вариант 2


def my_func(x=int(input('введите действительное положительное число ')),
            y=int(input('введие целое отрицательное число '))):
    i = 1
    c = x
    while i != abs(y):
        x = c * x
        i += 1
    else:
        print(1 / x)


my_func()
