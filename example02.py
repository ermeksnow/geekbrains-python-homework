number1 = int(input('введите число время в секундах'))
import time
print(time.strftime("%H:%M:%S", time.gmtime(number1)))
