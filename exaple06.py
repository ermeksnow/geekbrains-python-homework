start = int(input("сколько спортсмен пробежал в первый день тренировок?"))
finish = int(input("сколько спортсмену нужно пробежать для победы?"))
i = 1
while start < finish:
    start = start + (start*0.1)
    i+=1
else:
    print('дни спортивных мытарств',i)

