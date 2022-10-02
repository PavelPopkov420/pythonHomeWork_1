a = int(input('Введите число: '))

if a > 0 and a < 6:
    print('Будний день')
elif a == 6 or a == 7:
    print('Выходной')
else:
    print('Это не день недели')