from math import sqrt


def line_length(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
