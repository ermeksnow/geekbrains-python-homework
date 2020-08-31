def div(arg1, arg2):
        try:
            return arg1 / arg2
        except TypeError:
            return
arg1 = input('введите делимое')
arg2 = input('введите делитель')
while arg2 != 0:
    print(div(arg1, arg2))
    break
else:
    print('на ноль делить нельзя ')







