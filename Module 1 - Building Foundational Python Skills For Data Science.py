# Testing if Python works on my personal computer:
print("Hello, World!")

# Perform a simple calculation and print the result:
a = 5
b = 7
result = a + b
print(f"The result of {a} + {b} is {result}") 
# Result in terminal: The result of 5 + 7 is 12

# Define a list and loop through its elements
fruits = ["apple", "banana", "cherry"]
print("List of fruits:")
for n in fruits: # Instead of n I can write anything since code understands that it's an item in the list 
    print(n)

# A simple function that squares a number
def square(x):
    return x * x
# Use the function
number = 4
print(f"The square of {number} is {square(number)}") # Result: The square of 4 is 16

# Introduction 1: https://learning.oreilly.com/library/view/data-science-from/9781492041122/ch01.html#idm45635774220232

# In Python, a dict, short for "dictionary," is a built-in data type that represents a collection of key-value pairs. 
# It is also sometimes referred to as a "hash map" or an "associative array" in other programming languages. 
# Dictionaries are commonly used for storing and retrieving data efficiently, where each value is associated with a unique key.
# users is dict

# dict "users" represents employees at work: 

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# friendship_pairs (list) represents who is a friend with who:

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

print(friendships)
# Result: {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

# With append we are adding friends' ids next to the employee:
print(friendships)

# Result: {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 8], 7: [5, 8], 8: [6, 7, 9], 9: [8]}

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

print(number_of_friends(users[1])) # Result: 3

total_connections = sum(number_of_friends(user)
                        for user in users)      

print(total_connections) # Result: 24

num_users = len(users) # length of the users list

print(num_users) # Result: 10

avg_connections = total_connections / num_users   # 24 / 10 == 2.4

# Create a list (user_id, number_of_friends):
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

print(num_friends_by_id)
# Result: [(0, 2), (1, 3), (2, 3), (3, 3), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 1)]
# 0 has 2 friends, 1 have 3, etc.

num_friends_by_id.sort(                                # Sort the list
       key=lambda id_and_friends: id_and_friends[1],   # by num_friends
       reverse=True)                                   # largest to smallest

print(num_friends_by_id)
# Result: [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print(foaf_ids_bad(users[0]))

# Result: [0, 2, 3, 0, 1, 3]

print(friendships[0])  # Result: [1, 2]
print(friendships[1])  # Result: [0, 2, 3]
print(friendships[2])  # Result: [0, 1, 3]

# Counter - In Python, Counter is a class that counts the occurrences of elements in an iterable and returns the results as a dictionary-like object.

# Simple example: 
from collections import Counter                   # not loaded by default --seems that this row should go everywhere next to Counter
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = Counter(my_list)
print(counts)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})

from collections import Counter                   # not loaded by default --seems that this row should go everywhere next to Counter
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]     # For each of my friends,
        for foaf_id in friendships[friend_id]     # find their friends
        if foaf_id != user_id                     # who aren't me
        and foaf_id not in friendships[user_id]   # and aren't my friends.
    )

print(friends_of_friends(users[3]))               # Counter({0: 2, 5: 1})

# Another task. These are employees interest:

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# Defining the formula which will find employees who's interests will be added as input into the formula:

def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

print(data_scientists_who_like('Java')) #Result: [0, 5, 9]

# defaultdict - In Python, defaultdict is a dictionary subclass that automatically initializes new keys with a default value of your choice, 
# making it useful for tasks where you want to ensure that all keys have an initial value.

from collections import defaultdict
# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest)

# Result:
# defaultdict(<class 'list'>, {'Hadoop': [0, 9], 'Big Data': [0, 8, 9], 'HBase': [0, 1], 'Java': [0, 5, 9], 'Spark': [0], 
# 'Storm': [0], 'Cassandra': [0, 1], 'NoSQL': [1], 'MongoDB': [1], 'Postgres': [1], 'Python': [2, 3, 5], 
# 'scikit-learn': [2, 7], 'scipy': [2], 'numpy': [2], 'statsmodels': [2], 'pandas': [2], 'R': [3, 5], 'statistics': [3, 6], 
# 'regression': [3, 4], 'probability': [3, 6], 'machine learning': [4, 7], 'decision trees': [4], 'libsvm': [4], 'C++': [5], 
# 'Haskell': [5], 'programming languages': [5], 'mathematics': [6], 'theory': [6], 'Mahout': [7], 'neural networks': [7, 8], 
# 'deep learning': [8], 'artificial intelligence': [8], 'MapReduce': [9]})

# Keys are user_ids, values are lists of interests for that user_id.
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

print(interests_by_user_id)

# Result:
# defaultdict(<class 'list'>, {0: ['Hadoop', 'Big Data', 'HBase', 'Java', 'Spark', 'Storm', 'Cassandra'], 
# 1: ['NoSQL', 'MongoDB', 'Cassandra', 'HBase', 'Postgres'], 2: ['Python', 'scikit-learn', 'scipy', 'numpy', 'statsmodels', 'pandas'], 
# 3: ['R', 'Python', 'statistics', 'regression', 'probability'], 4: ['machine learning', 'regression', 'decision trees', 'libsvm'], 
# 5: ['Python', 'R', 'Java', 'C++', 'Haskell', 'programming languages'], 6: ['statistics', 'probability', 'mathematics', 'theory'], 
# 7: ['machine learning', 'scikit-learn', 'Mahout', 'neural networks'], 8: ['neural networks', 'deep learning', 'Big Data', 'artificial intelligence'], 
# 9: ['Hadoop', 'Java', 'MapReduce', 'Big Data']})

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

# Calculates which another user have same interest as input:

print(most_common_interests_with(users[0]))

# Result: Counter({9: 3, 1: 2, 8: 1, 5: 1})

# Another task:

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print(salary_by_tenure)

#Result: defaultdict(<class 'list'>, {8.7: [83000], 8.1: [88000], 0.7: [48000], 6: [76000], 6.5: [69000], 7.5: [76000], 2.5: [60000], 10: [83000], 1.9: [48000], 4.2: [63000]})

# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)

# Result: {8.7: 83000.0, 8.1: 88000.0, 0.7: 48000.0, 6: 76000.0, 6.5: 69000.0, 7.5: 76000.0, 2.5: 60000.0, 10: 83000.0, 1.9: 48000.0, 4.2: 63000.0}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
    
# Keys are tenure buckets, values are lists of salaries for that bucket.
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

print(salary_by_tenure_bucket)

# Result: defaultdict(<class 'list'>, {'more than five': [83000, 88000, 76000, 69000, 76000, 83000], 'less than two': [48000, 48000], 'between two and five': [60000, 63000]})

# Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
  tenure_bucket: sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# Explanation for .items() In Python, items() is a method that can be called on a dictionary object. It returns a view of the dictionary's key-value pairs as a sequence of tuples. 
# Each tuple contains two elements: the key and the corresponding value.

print(average_salary_by_bucket)

# Result: {'more than five': 79166.66666666667, 'less than two': 48000.0, 'between two and five': 61500.0}

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)

# Result
# big 3
# data 3
# java 3
# python 3
# learning 3
# hadoop 2
# hbase 2
# cassandra 2
# scikit-learn 2
# r 2
# statistics 2
# regression 2
# probability 2
# machine 2
# neural 2
# networks 2

print(words_and_counts)

# Result: Counter({'big': 3, 'data': 3, 'java': 3, 'python': 3, 'learning': 3, 'hadoop': 2, 'hbase': 2, 'cassandra': 2, 
# 'scikit-learn': 2, 'r': 2, 'statistics': 2, 'regression': 2, 'probability': 2, 'machine': 2, 'neural': 2, 'networks': 2, 
# 'spark': 1, 'storm': 1, 'nosql': 1, 'mongodb': 1, 'postgres': 1, 'scipy': 1, 'numpy': 1, 'statsmodels': 1, 'pandas': 1, 
# 'decision': 1, 'trees': 1, 'libsvm': 1, 'c++': 1, 'haskell': 1, 'programming': 1, 'languages': 1, 'mathematics': 1, '
# 'theory': 1, 'mahout': 1, 'deep': 1, 'artificial': 1, 'intelligence': 1, 'mapreduce': 1})

# https://learning.oreilly.com/videos/modern-python-livelessons/9780134743400/9780134743400-MOPY_01_00_00/
# Lesson 1: Building Foundational Python Skills for Data Analytics (C4, 1)

x=10
print(f'The answer is {x}') # Result: The answer is 10

# raise ValueError(f'Expected {x!r} to a float not a {type(x).__name__}')

from collections import Counter
print(Counter('red green blue red blue green green'.split()))

# Result: Counter({'green': 3, 'red': 2, 'blue': 2})

from statistics import mean, median, mode, stdev, pstdev

# Explanation between stdev and pstdev: The key difference between stdev (standard deviation) and pstdev (population standard deviation) is in 
# their application to data: stdev is used when working with a sample of data and corrects for bias by dividing by n-1 (Bessel's correction), 
# while pstdev is used when you have data for the entire population and divides by n without applying the correction, as it assumes no sampling error.

print(mean([50, 52, 53]))
print(stdev([50, 52, 53]))
print(pstdev([50, 52, 53]))

s = [10, 20, 30]

t= [40, 50, 60]

print(s + t)

s=[10, 5, 70, 2]
print(s.sort())

print(100 + (lambda x:x**2)(5) +50)

# Explanation: lambda x: x**2 defines an anonymous function, also known as a lambda function. This function takes one argument x and returns the square of x.
# (5) immediately calls (invokes) the lambda function with the argument 5. So, (lambda x: x**2)(5) calculates and returns the square of 5, which is 25.
# The expression 100 + 25 + 50 is evaluated, resulting in 175.

# PROD for using lambda:
# Conciseness: Lambda functions are very concise and can be defined in a single line of code. This can make your code more readable when the function is simple and short.

x=15
print(x>6)
print(x<10) # It is called Chained Comparissons

# Part 2: 

from random import *
print(random ()) # 0.23926123941024857
seed (8675309)
print(random ()) # 0.40224696110279223
seed (8675309)
print(random ()) # 0.40224696110279223

print(uniform(1000,1100)) # Result: 1051.0247177921592

print(triangular(1000, 1100)) #Result: 1058.9965313824887

print(gauss(1000, 1100))  # Result: 1572.563936827863

print(expovariate(20)) # Result: 0.05127656633162116

from statistics import mean, stdev

data = [triangular(1000, 1100) for i in range(1000)]

print(data)

print(mean(data)) # Result: 1048.697761431962

print(stdev(data)) # Result 20.11982549227617

data = [uniform(1000, 1100) for i in range(1000)]

print(data)

print(mean(data)) # Result: 1051.1525573532265

print(stdev(data)) # Result 28.52923129352503

data = [expovariate(20) for i in range(1000)]

print(data)

print(mean(data)) # Result: 0.05135273750430566

print(stdev(data)) # Result 0.05257849010975472

from random import choice, choices, sample, shuffle

outcomes = ['win', 'lose', 'draw', 'play again', 'double win']

print(choice(outcomes)) #double win

print(choices(outcomes, k=10)) #['play again', 'lose', 'win', 'play again', 'play again', 'double win', 'draw', 'win', 'double win', 'double win']

print(Counter(choices(outcomes, [5, 4, 3, 2, 1], k=1000)))

#Result: Counter({'win': 339, 'lose': 250, 'draw': 205, 'play again': 132, 'double win': 74})

print(shuffle(outcomes)) #ordering

print(outcomes) #['lose', 'play again', 'win', 'double win', 'draw']


print(choices(outcomes, k=5)) #['double win', 'double win', 'double win', 'double win', 'win']

#without duplicates:
print(sample(outcomes, k=5)) #['draw', 'play again', 'double win', 'win', 'lose']

print(sample(range(1, 57), k=6)) #[39, 22, 45, 42, 8, 54]

print(sorted(sample(range(1, 57), k=6))) #[19, 23, 29, 40, 42, 46]

# Lesson 2: Analyzing Data Using Simulations and Resampling (C2, 1)

# Six roulette spins:

from random import *
from statistics import *
from collections import *

# Six roulette wheels 18 black, 18 red, 2 green

choice(['red', 'red', 'red', 'black', 'black', 'black', 'green']) #too much to write

population = ["red"]*18 + ["green"]*2 + ["white"]*18

print(choice(population)) #white

print([choice(population) for i in range(6)]) #['white', 'green', 'white', 'red', 'white', 'red']

print(Counter([choice(population) for i in range(6)])) #Counter({'white': 3, 'red': 3})

print(choices(population, k=6)) #['red', 'red', 'white', 'red', 'white', 'red']

print(Counter(choices(["red", "green", "white"], [18, 2, 18], k=6))) #Counter({'red': 3, 'white': 2, 'green': 1})

deck = Counter(tens = 16, low = 36)

print(list(deck.elements()))

# ['tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'tens', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low']

print(deck)

deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, 52)
remainder = deal[20:]

print(Counter(deck)) #Counter({'low': 36, 'tens': 16})
print(Counter(deal)) #Counter({'low': 36, 'tens': 16})
print(Counter(remainder)) #Counter({'low': 23, 'tens': 9})

#Coin spin:

population_coins = ['heads', 'tails']
wgt = [6,4]
cumwgt= [0.60, 1.00]

print(choices(['heads', 'tails'], [0.60, 1.00], k=7))

#['tails', 'tails', 'tails', 'tails', 'heads', 'tails', 'tails']

print(choices(['heads', 'tails'], [0.60, 1.00], k=7).count('heads')) #3

trial = lambda: choices(['heads', 'tails'], [0.60, 1.00], k=7).count('heads') >= 5 #3

print(trial()) #false

n= 100000

print(sum(trial() for i in range(n))/n) #0.074

from math import factorial as fact

print(fact(4)) #24

def comb(n, r):
    return fact(n)/fact(r)/fact(n-r)

print(comb(10, 3)) #120

#binomial theorem:

ph = 0.6

#what are the chances to get 5 heads of 7 spins:

print(ph **5 * (1 - ph) **2 * comb(7, 5)) #0.2612736

print(ph **6 * (1 - ph) **1 * comb(7, 6)) #0.13063679999999997

print(ph **7 * (1 - ph) **0 * comb(7, 7)) #0.027993599999999993

#Mathematical approach also works fine, but if there were 70k spins and we needed heads for 42k times, then it would become super large

# Does the median of five fall in the middle of two quartiles?

print(sample(range(100000), 5)) #[1164, 5190, 66777, 22460, 3212]

print(median(sample(range(100000), 5))) #53279

print(sorted(sample(range(100000), 5))) #[7448, 27534, 35875, 55682, 93385]

print(sorted(sample(range(100000), 5))[2]) #52283

n = 100000

print(n)
print(n//4) #25000
print(n*3//4) #75000
print(n//4 < median(sample(range(100000), 5)) <= 3*n//4) #False

# 25000 < 53279 <= 75000.0

trial = lambda : n//4 < median(sample(range(100000), 5)) <= 3*n//4

print(sum(trial() for i in range(n)) / n) #0.79171