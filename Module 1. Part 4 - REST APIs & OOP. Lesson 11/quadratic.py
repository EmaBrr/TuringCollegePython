# Lesson 11: Testing with PyTest, Itertools, Hypothesis, Pyflakes, MyPy and Data Validators (C2, 1)

# https://en.wikipedia.org/wiki/Quadratic_equation

import math 
from typing import Tuple

def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    '''
        Compute the root of the quadratic equation:
            ax^2 + bx + c = 0
        Written in Python as:
            a*x**2 + b*x + c == 0
        For example:
            >>> x1, x2 = quadratic(a = 8, b = 22, c = 15)
            >>> float(x1)
            (-1.25+0j)
            >>> float(x2)
            (-1.5+0j)
            >>> 8*x1**2 + 22*x1 +15
            0j
            >>> 8*x2**2 + 22*x2 + 15
            0j

    '''
    discriminant = math.sqrt(b**2.0 - 4.0*a*c) # 4.0 is faster than 4 in floating point calculation
    x1 = (-b + discriminant)/(2.0 * a)
    x2 = (-b - discriminant)/(2.0 * a)
    return x1, x2

# Pyflakes gives fewer false posiives than other lint tools

x1, x2 = quadratic(a=8, b=22, c=15)
print(x1) #-1.25
print(x2) #-1.5
print(8*x1**2+22*x1+15) #0.0

# print(help(quadratic))

# Doctest validate docstring with example and are effortless to create
# it says what was expected from the comment and what we got, so how many failures
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

# mypy '.\Module 1. Part 4 - REST APIs & OOP. Lesson 11.py'    
# pyflakes '.\Module 1. Part 4 - REST APIs & OOP. Lesson 11.py'

# py.test and nose takes less effort than unittest
