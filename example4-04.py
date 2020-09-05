from lesson04 import my_mod
my_list = (my_mod.func_ran())
print(my_list)
my_list2=[x for x in my_list if my_list.count(x) == 1]
print(my_list2)


