'''
Определите функцию, которая принимает координаты отрезков
x1, x2, y1, y2
Функция возращает "Да", если они пересекаются
или возращает "Нет"
'''

def find_intersection(x1, x2, y1, y2) -> str:
    points_x = set()
    points_y = set()

    if x1 < x2:
        step = 1
    elif x1 > x2:
        step = -1
    else:
        step = 0
    if step:
        for i in range(min((x1, x2)), max((x1, x2)) + 1, step):
            points_x.add(i)
    else:
        points_x.add(x1)

    if y1 < y2:
        for i in range(y1, y2 + 1, 1):
            points_y.add(i)
    elif y1 > y2:
        for i in range(y1, y2 + 1, -1):
            points_y.add(i)
    else:
        points_y.add(y1)


print(find_intersection(5, 10, 11, 20))