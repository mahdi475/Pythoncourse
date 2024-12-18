import math

def rectangle_area():
    a = int(input("Width of the rectangle: "))
    b = int(input("Height of the rectangle: "))
    area = a * b
    return area

def circle_area():
    diameter = int(input("Diameter of the circle: "))
    radius = diameter / 2
    area = int(math.pi * radius * radius)
    return area

def triangle_area():
    a = int(input("Width of the triangle: "))
    b = int(input("Height of the triangle: "))
    area = a * b / 2
    return area
