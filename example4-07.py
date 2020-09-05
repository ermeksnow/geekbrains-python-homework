def fact(n):
    import math
    for x in range(1,n):
        yield math.factorial(x)
    #return math.factorial(x for x in range(1,n))

    #math.factorial(a)
n = int(input('введите число обозначающие факторил дальше которого функция не отработает'))+1  #+1 добавленно для компенсации верхней границы ,так как число n не включается
for x in fact(n):
    print(x)



