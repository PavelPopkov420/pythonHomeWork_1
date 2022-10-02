print('Введите координаты А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

import math

sqrt = round(math.sqrt((x_B - x_A) ** 2 + (y_B - y_A) ** 2),2)

print(f'Расстояние междк точками = {sqrt}')