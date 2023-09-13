import math


class Figure:
    a: int

    def area(a) -> object:
        s = pow(a, 2)
        return s


class Circle(Figure):
    r: int

    def area(r):
        s = math.pi * pow(r, 2)
        return round(s, 2)


class triangle(Figure):
    a: int
    b: int
    c: int

    def tp_tria(a, b, c):
        if pow(c, 2) == a * a + b * b:
            tp = 1
        else:
            tp = 0
        return tp

    def area(a: int, b: int, h: None):
        if triangle.tp_tria(a, b, c=0) == 1:
            print('Вы ввели строны прямоугольного  треугольника. Рассчитываю площадь...')
            s = a * b / 2
        elif triangle.tp_tria(a, b=0, c=0) == 0:
            print('Вы  ввели стороны обычного треугольника. Рассчитываю площадь....')
            h = int(input('Введите высоту'))
            s = a * h / 2
            return s
