first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first != second and first != third and third != second:
    print(0)
elif first == second == third:
    print(3)
else:
    print(2)