
from functools import reduce

my_list =[x for x in range(100,1001) if x % 2== 0]
composition= reduce(lambda x,y:x*y,my_list)

print(my_list)
print(composition)

