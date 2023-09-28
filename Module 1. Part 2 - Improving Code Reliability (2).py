# Improving Reliability with MyPy and Type Hinting

# KEY THINGS TO REMEMBER:
# fsum is more accurate than sum
# defaultdict is used for grouping
# key functions work eith min max sorted nsmallest nlargest groupby and merge
# z star is used for transpose 2d data zip(*data)
# convert an iterator into a list with list(it)
# 


from typing import *
from collections import OrderedDict, deque, namedtuple
import secrets

# Tools:
# mypy
# pyflakes
# hypothesis
# unittest -> nose py.test

# x = 10 #type: int
x: int = 10

# We can check it in terminal with: python -m mypy b.py

def f(x,y):
    return x + y

print(f(10,20)) # 30

# print(f(10,'world')) # error

# improving:
def g(x:int,y:int) -> int:
    return x + y

# print(g(10,'world')) # error

# x = {} # dictionary, but when we import this OrderedDict mypy would expect it to be OrderedDict

# y = OrderedDict()

def k(x: Sequence[int])-> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

k([10,20,30])
# print()
# print(h('abcdef'))
# print(h((11,12,13)))
# print(h(None))

def h(x: List[int])-> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

h([10,20,30])
# h((11,12,13))
# print()
# print(h('abcdef'))
# print(h((11,12,13)))
# print(h(None))

hts = [91.7, 102.5, 97.5] #type: List[float]
person = ('Reymond', 5 * 12 + 12) #type: Tuple[str, float]
info = ('Pearson', 'Course', 'Python', 'Raymond') #Tuple[str, str, str]

def u(x:int,y:Optional[int]=None) -> int:
    if y is None:
        y=20
    return x + y

fifo= deque() #type: deque

# Point = namedtuple('Point', [('x', int), ('y', int)])


# A tuple is a data structure in programming that is used to store an ordered collection of elements. Tuples are similar to lists in many ways, but they have one key difference: tuples are immutable, which means their elements cannot be changed after they are defined.

print(1.1 + 2.2) #3.3000000000000003

1.1 + 2.2 == 3.3 #false

sum([0.1]*10) #0.99999999999999

from math import fsum

print(fsum([0.1]*10)==1.0) #true, so the fsum eliminated the rounding error

print(38/5) # 7.6

from collections import defaultdict
# d= {'raymon':'red'}
e = defaultdict(lambda:'black')
e['raymond'] = 'red'

# print(d) #{'raymon': 'red'}
print(e) #defaultdict(<function <lambda> at 0x000001D2286CE480>, {'raymond': 'red'})

set() #()
list() #[]
dict() #{}

d=defaultdict(set) #sets eliminate duplicated, list doesn't
d['t'].add('tom')
d['m'].add('marry')
d['t'].add('tim')
d['t'].add('tom')
d['m'].add('martin')

print(d)

#{'raymon': 'red'}
# defaultdict(<function <lambda> at 0x0000018C4DDCA520>, {'raymond': 'red'})
# defaultdict(<class 'set'>, {'t': {'tom', 'tim'}, 'm': {'marry', 'martin'}})   

#Defaultdict created a new container to store elements with a common feature

from pprint import pprint

pprint(d, width=40)

# defaultdict(<class 'set'>,
#             {'m': {'martin', 'marry'},
#              't': {'tim', 'tom'}})

a=defaultdict(list) #sets eliminate duplicated, list doesn't
a['t'].append('tom')
a['m'].append('marry')
a['t'].append('tim')
a['t'].append('tom')
a['m'].append('martin')

print(a) #defaultdict(<class 'list'>, {'t': ['tom', 'tim', 'tom'], 'm': ['marry', 'martin']})

names = ''' david betty susan mary darlee dandy davin shelly becky beatrice tom michael wallace'''.split()

print(names)

# ['david', 'betty', 'susan', 'mary', 'darlee', 'dandy', 'davin', 'shelly', 'becky', 'beatrice', 'tom', 'michael', 'wallace']

d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)

pprint(d)

#Result:
# defaultdict(<class 'list'>,
#             {'b': ['betty', 'becky', 'beatrice'],
#              'd': ['david', 'darlee', 'dandy', 'davin'],
#              'm': ['mary', 'michael'],
#              's': ['susan', 'shelly'],
#              't': ['tom'],
#              'w': ['wallace']})


d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)

pprint(d)

#Result:
# defaultdict(<class 'list'>,
#             {3: ['tom'],
#              4: ['mary'],
#              5: ['david', 'betty', 'susan', 'dandy', 'davin', 'becky'],
#              6: ['darlee', 'shelly'],
#              7: ['michael', 'wallace'],
#              8: ['beatrice']})


#same as in SQL: SELECT NAME FROM NAMED ORDER BY LEN(NAME)

pprint(sorted(names, key=len))

#Result:
# ['tom',
#  'mary',
#  'david',
#  'betty',
#  'susan',
#  'dandy',
#  'davin',
#  'becky',
#  'darlee',
#  'shelly',
#  'michael',
#  'wallace',
#  'beatrice']

# TOPIC: TRANSPOSING WITH ZIP () AND STAR-ARGS

print(list(zip('abcdef', 'gfthilkok')))
# [('a', 'g'), ('b', 'f'), ('c', 't'), ('d', 'h'), ('e', 'i'), ('f', 'l')]

from itertools import zip_longest
print(list(zip_longest('abcdef', 'gfthilkok', fillvalue='x')))

# [('a', 'g'), ('b', 'f'), ('c', 't'), ('d', 'h'), ('e', 'i'), ('f', 'l')]
# [('a', 'g'), ('b', 'f'), ('c', 't'), ('d', 'h'), ('e', 'i'), ('f', 'l'), ('x', 'k'), ('x', 'o'), ('x', 'k')]

m = [
    [10,20],
    [30,40],
    [50,60],
]

pprint(list(zip(m)), width=15)

# [([10, 20],),
#  ([30, 40],),
#  ([50, 60],)]

pprint(list(zip(*m)), width=15) # we can retransform matrices with this method

# [(10, 30, 50),
#  (20, 40, 60)]

for row in m:
    print(row)

for row in m:
    for col in row:
        print(col)    
# 10
# 20
# 30
# 40
# 50
# 60  

# LESSON 4
from pprint import pprint

points = [
    (10,41,23),
    (22,30,29),
    (11,42,5),
    (20,32,4),
    (12,40,12),
    (21,36,23),
]

pprint(points)

# print(mean(point))

def f(data):
    return sum(data) / len(data)

g = f([12,13,13])
# mean(1,2,3)

print(g)

from math import fsum, hypot, sqrt
from typing import Iterable, Tuple

def f(data: Iterable[float]) -> float:
    #accurate arithmetic mean
    data = list(data)
    return fsum(data) / len(data)

g = f([12,13,13])
# mean(1,2,3)

print(g)

print(hypot(3,4)) #5.0

p= (10,41,23)
q= (22,30,20)
list(zip(p,q))

def dist(p, q):
    return [x - y for x, y in zip(p, q)]

def dist(p, q):
    #euclidean distance function for multidimentional data
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

from dis import * #what does it do??

def dist(p, q, fsum=fsum, sqrt=sqrt, zip=zip):
    #euclidean distance function for multidimentional data
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

print(dis(dist))

def dist(p, q, fsum=fsum, sqrt=sqrt, zip=zip):
    #euclidean distance function for multidimentional data
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

print(dis(dist))





for point in points:
    print(point, dist(point, (9,39,20)))



# The task: let's say we have 3D and there are two suns that will be called centroids, and there are planets and we want to know to which sun it's connected (which is the closest)
from collections import defaultdict
from math import fsum, hypot, sqrt    
from typing import Iterable, Tuple

Point = Tuple[int, ...]

def dist(p: Point, q: Point) -> float:
    # Euclidean distance function for multidimensional data
    return sqrt(sum((x - y) ** 2 for x, y in zip(p, q)))

centroids = [(9, 39, 20), (12, 36, 25)]
point = (11, 42, 5)

# Calculate distances for each centroid individually
distances = [dist(point, centroid) for centroid in centroids]
print(distances)

#[15.427248620541512, 20.904544960366874]

print(min(centroids, key= lambda centroid: dist(point, centroid))) #(9, 39, 20)

from functools import partial

print(pow(2,5))

twopow = partial(pow, 2)
twopow(5)

min(centroids, key= partial(dist, point))

def assign_data(centroids, data):
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return d

pprint(assign_data(centroids, points), width=45)

# Result:
# defaultdict(<class 'list'>,
#             {(9, 39, 20): [(10, 41, 23),
#                            (11, 42, 5),
#                            (20, 32, 4),
#                            (12, 40, 12)],
#              (12, 36, 25): [(22, 30, 29),
#                             (21, 36, 23)]})

groups = [
    [(10, 41, 23),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12)],
    [(22, 30, 29),
     (21, 36, 23)]
]

pprint(groups)

# Result:
# [[(10, 41, 23), (11, 42, 5), (20, 32, 4), (12, 40, 12)],
#  [(22, 30, 29), (21, 36, 23)]]

group = [(10, 41, 23), (11, 42, 5), (20, 32, 4), (12, 40, 12)]

# We want to calculate the average, so we need to move together all those cordinates:

pprint(list(zip(*group)))

from statistics import mean
# Result:
# [(10, 11, 20, 12), (41, 42, 32, 40), (23, 5, 4, 12)]
# [(x, x, x, x), (y, y, y, y), (z, z, z, z)]

pprint(list(map(mean, zip(*group))))

#  Result: [13.25, 38.75, 11]

pprint([tuple(map(mean, zip(*group))) for group in groups])

#LESSON 4 PART 2

