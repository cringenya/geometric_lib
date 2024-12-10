
def area(a):
    '''Принимает длину стороны квадрата, возвращает его площадь;
       Ex: area(5) -> 25 '''
    if isinstance(a, int) or isinstance(a, float):
        if (a < 0) :
            return "Error: negative value"
        return a * a
    else:
        return "Error: wrong data type"


def perimeter(a):
    '''Принимает длину стороны квадрата, возвращает его периметр;
       Ex: perimeter(5) -> 20 '''
    if isinstance(a, int) or isinstance(a, float):
        if (a < 0) :
            return "Error: negative value"
        return 4 * a
    else :
        return "Error: wrong data type"
