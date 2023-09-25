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
print(users[0])
test_calling_function = foaf_ids_bad(users[0])
print(test_calling_function)
print(foaf_ids_bad(users[0]))
print(friendships[0])  # [1, 2]
print(friendships[1])  # [0, 2, 3]
print(friendships[2])  # [0, 1, 3]
from collections import Counter                   # not loaded by default
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
def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

from collections import defaultdict
# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interests for that user_id.
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]
# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
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
# Keys are tenure buckets, values are average salary for that bucket.
average_salary_by_bucket = {
  tenure_bucket: sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
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






print('hello world')

x=10
print(f'The answer is {x}')

# raise ValueError(f'Expected {x!r} to a float not a {type(x).__name__}')

from collections import Counter
d={}
d=Counter()
d
print(Counter('red green blue red blue green green'.split()))

from statistics import mean, median, mode, stdev, pstdev

# stdev dalina iš kiek yra skaičių, o pstdev dalina iš n-1

print(mean([50, 52, 53]))

print(stdev([50, 52, 53]))
print(pstdev([50, 52, 53]))

s = [10, 20, 30]

t= [40, 50, 60]

print(s+t)

s=[10, 5, 70, 2]
print(s.sort())

# Lambda --> partial objects itemgetter, arttrgetter

print(100 + (lambda x:x**2)(5) +50)

x=15
print(x>6)
print(x<10) #chained comparissons