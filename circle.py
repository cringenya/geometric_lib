import math


def area(r):
    '''Принимает радиус круга, возвращает площадь, равную pi*r^2;

       Ex: area(2) -> 12,5663706144 '''	
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга, возвращает периметр, равный 2*pi*r;

       Ex: perimeter(3) -> 18,8495559215 ''' 
    return 2 * math.pi * r

