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

# Sequence: A sequence is a general term for an ordered collection of elements. It can refer to both lists and tuples. Sequences are iterable and indexable, meaning you can access their elements by position. Lists and tuples are examples of sequences, but lists are mutable (modifiable), while tuples are immutable (unchangeable).

# List: A list is a mutable and ordered collection of elements enclosed in square brackets []. Lists allow you to add, remove, or modify elements after creation. They are commonly used for dynamic collections of items where the order and content may change during the program's execution.

# Dictionary (dict): A dictionary is an unordered collection of key-value pairs enclosed in curly braces {}. Each key in a dictionary maps to a corresponding value, and you can use the key to access the associated value. Dictionaries are useful for storing and retrieving data based on unique keys and are often used for implementing associative arrays or mappings.

# zip(*group) can be changed to transposed

# LESSON 5

# defaultdict -- TOPIC

from collections import defaultdict #collections is a module

# explanation of defaultdict:
# When you create a defaultdict, you specify a default factory function as an argument. This function determines the default value for any new keys added to the dictionary.
# When you access a key that doesn't exist in the defaultdict, it automatically creates that key and assigns it a default value generated by the factory function.

d= defaultdict(list)
d['raymond'].append('red')
d['rachel'].append('blue')
d['matthwe'].append('yellow')
print(d)

from pprint import pprint

pprint(d)

d['raymond'].append('mac')
d['rachel'].append('pc')
d['matthwe'].append('vtec')

# We can convert defaultdict to regular one for normal use

print(dict(d))

# Defaultdict could be used for grouping and accumulation

# Model one to many: dict(one, list_of_many)
e2s= {
    'one':'uno', 
    'two':'tres', 
    'three': 'tres', 
    'trio': 'tres',
    'free': ['libres', 'gratis']
}

pprint(e2s, width=40)

pprint(e2s, width=40)

s2e = defaultdict(list)
for eng, spanwords in e2s.items():
    if isinstance(spanwords, list): # in the video this IF part was not added therefore it didn't work
        for span in spanwords:
            s2e[span].append(eng)
    else:
        s2e[spanwords].append(eng)  # Use spanwords as the key

pprint(dict(s2e), width=40)  # Convert defaultdict to a regular dictionary for prettier printing


# One to one called bijetion by mathematicians

e2s = dict(one='uno', two = 'dos', three = 'tres')

span_to_eng = {span: eng for eng, span in e2s.items()}

print(span_to_eng) 

# result: {'uno': 'one', 'dos': 'two', 'tres': 'three'}

# LESSON 5 PART 2

import glob
print(glob.glob('*.txt')) #Result: []

# glob.glob('*.txt'): This line calls the glob.glob() function with the argument '*.txt'. The *.txt pattern is a wildcard pattern that matches all files with the .txt file extension in the current directory.

# Global wildcard expansion -> os.expand_wildcards()

with open('test.txt', encoding='utf-8') as f:
    print(f.read())

# It prints everything what's in that file

it = iter('abcdefg')
print(it) #Result: <str_ascii_iterator object at 0x0000018E455409A0>

print(next(it)) #Result: a

print(list(it)) #Result: ['b', 'c', 'd', 'e', 'f', 'g']

# If you have CSV file and want to split the information:

import csv
# with open('filename.csv', encoding='utf-8') as f:
#     for row in csvreader(f):
            # print(row)

t = ('Raymond', 'Hettinger', 54, 'python@gmail.com')
print(type(t)) #<class 'tuple'>

print(len(t))

# Let's assign the name of "column" for the info inside tuple:

fname, lname, age, email = t

print(fname) #Raymond

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow'.split()
cities = 'austin dallas austin houston chicago dallas austin'.split()

# Loop idioms

for i in range(len(names)):
    print(names[i].upper())

# Result:
# RAYMOND
# RACHEL
# MATTHEW

for name in names:
    print(name.upper())


for i in range(len(names)):
    print(i+1, names[i].upper())

# Result:
# 1 RAYMOND
# 2 RACHEL
# 3 MATTHEW

for i, name in enumerate(names, start= 1):
    print(i, name)

# Result:
# 1 raymond
# 2 rachel
# 3 matthew

for color in reversed(colors):
    print(color)

# yellow
# blue
# red

print(names)
print(colors)

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], colors[i])

# raymond red
# rachel blue
# matthew yellow

for color in sorted(colors, key = len): #in this case it sortes according to the lenght of the word
    print(color)


# Eliminating duplicates:
print(cities)
# ['austin', 'dallas', 'austin', 'houston', 'chicago', 'dallas', 'austin']

for city in cities:
    print(city)

# austin
# dallas
# austin
# houston
# chicago
# dallas
# austin

#SAME AS SELECT DISTINCT CITY FROM CITIES ORDER BY CITY

for city in enumerate(reversed(sorted(set(cities)))):
    print(city)

# (0, 'houston')
# (1, 'dallas')
# (2, 'chicago')
# (3, 'austin')    

for i, city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)

# 0 HOUSTON
# 1 DALLAS
# 2 CHICAGO
# 3 AUSTIN

import collections 
c= collections.Counter()
c['blue'] += 1
c['blue'] += 1
c['red'] += 1

print(c) #Counter({'blue': 2, 'red': 1})

most_common = c.most_common(1)  # Use most_common(1) instead of most.common(1)
print(most_common) #[('blue', 2)]

somethingelse = list(c.elements())  
print(somethingelse) #['blue', 'blue', 'red']

# Assertions:

assert 5 + 3 ==8
# assert 5 + 3 ==10 #error




