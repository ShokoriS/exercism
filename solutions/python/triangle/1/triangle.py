# Determine the type of a triangle
def conditions(a, b, c):

    all_zeros = all(map(lambda x: x > 0, (a, b, c)))
    all_equal_or_greater = all((a + b >=c, b + c >=a, a + c >= b))
    return all_zeros and all_equal_or_greater

def equilateral(sides):
    a, b, c = sides    
    if conditions(a, b, c):
        return a == b == c 
    return False


def isosceles(sides):
    a, b, c = sides
    if conditions(a, b, c):
        return any((a == b, b == c, c == a))
    return False

def scalene(sides):
    a, b, c = sides
    if conditions(a, b, c):
    
        return all((a !=b, b != c, c != a))
    return False 

