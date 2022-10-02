a = int(input("Введите номер четверти:  "))

if   a == 1:
    print('x от 0 до +∞, y от 0 до +∞') 
elif a == 2:
    print('x от 0 до -∞, y от 0 до +∞')  
elif a == 3: 
    print('x от 0 до -∞, y от 0 до -∞')
elif a == 4:
    print('x от 0 до +∞, y от 0 до -∞')
else:
    print("Ошибка, попробуйте снова")