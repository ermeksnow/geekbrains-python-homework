import sys
from lesson04 import my_mod

try:
    file, clock, rate , bonus = sys.argv
except ValueError:
        print("некоректные данные")


my_mod.my_salary(clock, rate, bonus)


