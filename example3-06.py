def int_func(a):
    print(a.capitalize())


# a = input('едите слово')
# int_func(a)
def int_func2():
    b = input('введите слова в нижнем регистре через пробел ').split()
    print(b)
    for i in b:
        int_func(i)


int_func2()
