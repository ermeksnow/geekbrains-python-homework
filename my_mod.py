#задание 1  расчет зароботной платы
def my_salary(clock, rate, bonus):
    salary = (int(clock) * int(rate)) + int(bonus)
    print(salary)


#задание2
#генерация списка из 10 позиций со значениями 0  до -50
def func_ran():
    import random
    list_one = []
    for x in  range(1,11) :
        list_one.append(random.randint(0, 50))
    else:
        #print(list_one)
        return list_one



