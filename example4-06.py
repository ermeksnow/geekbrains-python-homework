#задача 6.1
def int_1(i):
    from itertools import count
    list_one = []
    print('число начала списка',i)
    for x in count(i):
        if x > 10:
            break
        else:
            list_one.append(x)
    print(list_one)
int_1(6)


#задача 6.2
def int_2(repeat):
    from itertools import cycle
    lisi_int_2=[1,2,3,4,5,6,7,8,9,0]
    list_final=[]
    i=1
    print(repeat,'количество повторений цикла')
    for x in cycle(lisi_int_2):
        if i< repeat*len(lisi_int_2)+1:   # +1 добавлена чтобы уровнять количестро индксов в len(lisi_int_2)
            list_final.append(x)
            i+=1
        else:
            break
    print(list_final)
int_2(3)
