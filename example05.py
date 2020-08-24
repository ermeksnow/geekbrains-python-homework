reserved = int(input('введите количество полученных фирмой денег'))
spent = int(input('введите количество потраченных денег'))
if reserved > spent:
    print('фирма работает с прибылью')
    print('рентабельность', (reserved - spent))
    peoples = int(input('введите число сотрудников'))
    print('рентабельность одного сотрудника', ((reserved - spent) / peoples))
elif reserved == spent:
    print('выручка равна затратам')
else:
    print('зартраты больше выручки')


