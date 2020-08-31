def my_func():
    sum_final = 0
    q = True
    while q == True:
        a = input('Введите числа через пробел ,если хотите закончить нажмите #').split()
        print(a)
        for i in a:
            if i == '#':
                q = False
                break

            else:
                sum_final = sum_final + int(i)
        print(sum_final)
my_func()