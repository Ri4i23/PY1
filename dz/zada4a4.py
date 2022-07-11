# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите четверть: '))

if quarter == 1:
    coordinate = 'x > 0, y > 0'
elif quarter == 2:
    coordinate = 'x < 0, y > 0'
elif quarter == 3:
    coordinate ='x < 0, y < 0'
elif quarter == 4:
    coordinate = 'x > 0, y < 0'
else:
    coordinate='Пятой четверти нет'
print(coordinate)