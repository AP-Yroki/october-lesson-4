def distance(x1=0,y1=0,x2=0,y2=0):
    dst = ((y2 - y1)**2 + (x2 -x1) ** 2) ** 0.5
    return dst

x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))

res = distance(x2 = x2, y2 = y2, x1 = x1, y1 = y1)
print(f'Расстояние между точкой ({x1}, {y1}) и ({x2}, {y2}) равно {res}')