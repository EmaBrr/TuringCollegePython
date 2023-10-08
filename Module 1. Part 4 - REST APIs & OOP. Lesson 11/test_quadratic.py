# import py.test # Doesn't work
from quadratic import quadratic
import itertools 
from itertools import *

for t in product('ABC', 'DE', 'xyz'):
    print(t)

for r in permutations('Love'):
    print(r)

for r in permutations('Love', 2):
    print(r)

for r in combinations('Love', 2):
    print(r)


def test_quadratic():
    x1, x2 = quadratic(a=8, b=22, c=15)
    assert 8*x1**2 + 22*x1 +15 == 0
    assert 8*x2**2 + 22*x2 + 15 ==0

# def test_qudratic_types():
#     with py.test.raises(TypeError):
#         quadratic(a=8, b='hello', c=15)   
#     with py.test.raises(TypeError):
#         quadratic(a=8, b=8, c=15, d=4)  

def test_torture_test():
    args = [10, 0, 1, 18, -5, -1, 0.5, -1,5]
    for t in itertools.permutations(args, 3):
        x1, x2 = quadratic(*t)