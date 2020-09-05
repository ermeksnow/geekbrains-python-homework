from lesson04 import my_mod
list_1 = (my_mod.func_ran())     #импортируем функцию генерации списка
print('сгенерированный список',list_1)                   # выводим сгенерированный список
list_2=[]
i=0
while i+1 != len(list_1):
    if list_1[i] < list_1[i + 1]:
        list_2.append(list_1[i + 1])
        i += 1
    else:
        i+=1
        continue
print(i)
print(list_2)

