x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))

if x > 0 and y > 0:
    print('Четверть №1')
elif x > 0 and y < 0:
    print('Четверть №4')
elif x < 0 and y < 0:
    print('Четверть №3')
elif x < 0 and y > 0:
    print('Четверть №2')
else:
    print('Ошибка')