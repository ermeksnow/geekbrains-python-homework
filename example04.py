# number = input('Введите число ')
# print(max(number))                                  использование maх  показалась наиболее рациональным

number = input('Введите целое положительное число ')
i = 0
while number[i] != (max(number)):
    i = i + 1
else:
    print('наибольшая цифра в числе ', number[i])
