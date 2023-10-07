# Lesson 6: Applying Cluster Analysis to a Real Dataset (C2, 1.5)

# We will analyse congressional dataset with key means

from typing import NamedTuple, DefaultDict
import csv
# from kmeans import k_means, assign_data
from collections import defaultdict # namedtuple - removed when added above with capital letters, defaultdict for data accumulation
from pprint import pprint
import glob

# Senator = namedtuple('Senator', ['name', 'party', 'state'])

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
VoteValue = int
# Load the votes which were arranges by topic and acumulate votes by senator
vote_value= {'Yea': 1, 'Nay' : -1, 'Not Voting' : 0}   #Type: Dict[str, VoteValue]
accumulated_record = defaultdict(list)                  #Type: DefaultDict[Senator, List[VoteValue]]
for filename in glob.glob('congress_vot*.csv'):
    # with open('congress_votes_118-2023_h515.csv', encoding='utf-8') as f:
    with open(filename, encoding='utf-8') as f:  
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote]) # vote_value is a list, but we will need a tuple since we will use keys

# Transform the record into plain dict that maps to tuple of votes

record = {senator: tuple(votes) for senator, votes in accumulated_record.items()} # Type: Dict[Senator, VoteHistory]]
pprint(record, width=500)

# Use k-means to locate the cluster centroids from pattern of votes, asssign each senator to the nearest cluster
# centroids = k_means(record.values(), k=3)
# pprint(accumulated_record, width=500)

# ['person', 'state', 'district', 'vote', 'name', 'party'] headers

# print(senator[0]) # Rep. Jennifer McClellan [D]
# print(senator.name) # Rep. Jennifer McClellan [D]

# Lesson 6. Part 2. K_MEANS DOESN'T WORK
# NUM_SENATORS = 100
# # Reverse mapping from a vote history to a list of senators who voted that way
# votes_to_senators = defaultdict(list)   # type: DefaultDict[VoteHistory, List[Senator]]
# for senator, votehistory in record.items():
#     votes_to_senators[votehistory].append(senator)
# assert sum(len(cluster) for cluster in votes_to_senators()) ==NUM_SENATORS

# [len(cluster) for cluster in votes_to_senators.values()]

# # Display the clsuters and the members (senators) of each cluster

# for i, votes_in_cluster in enumerate(clustered_votes_values(), start = 1):
#     print(f'========= Voting Cluster #{i} ============'.format(i=i))
#     for votes in set(votes_in_cluster): #putting everything into set in order to removed dublicates
#         for senator in votes_to_senators[votes]:
#             print(senator)

# The bigger the data set, the better differentiation and the better k-means work. 

# Lesson 7: Gearing-up for a Publisher/Subscriber Application (C2, 1)

print('hello')
print('theRaymondWay\N{trade mark sign}')  # theRaymondWay™

s = 'L' + chr(246) + 'wis'
t = 'L' + chr(111) + chr(776) + 'wis'

# Result:
# Löwis
# Löwis

print(s)
print(t)

print([ord(c) for c in s]) # [76, 246, 119, 105, 115]
print([ord(c) for c in t]) # [76, 111, 776, 119, 105, 115]

s==t # false

import unicodedata
u = unicodedata.normalize('NFC', t)
print([ord(c) for c in u]) #[76, 246, 119, 105, 115]

# Named Tuples
import collections
Person = collections.namedtuple('Person', ['frame', 'lname', 'age', 'email'])

p = Person('Raymond', 'hettinger', 54, 'raymondexample.com')

print(p)

#Person(frame='Raymond', lname='hettinger', age=54, email='raymondexample.com') 

isinstance(p, tuple) #true

len(p) #4

a, b, c, d = p

p[:2]
p[0]

# Sorted data

import bisect #searching inside of ranges

# Hastables is better searching tool

cuts = [60, 70, 80, 90]
grades = 'FDCBA'

print(grades[bisect.bisect(cuts, 76)]) # C

print([grades[bisect.bisect(cuts, score)] for score in [76,92,80,70,69,91,99,100]])

# Result:
# ['C', 'A', 'B', 'C', 'D', 'A', 'A', 'A']

print(sorted([10,5,20])) #[5, 10, 20]

print(sorted([10,5,20]+[1,11,25])) #[1, 5, 10, 11, 20, 25]

a = [1, 11, 25]
b = [5, 10, 20]
c = [2, 15, 21]

sorted(a + b + c)

from heapq import merge
print(list(merge(a, b, c))) #[1, 2, 5, 10, 11, 15, 20, 21, 25]

it = merge(a, b, c)

print([it]) # [<generator object merge at 0x000002659800CE00>]

print(next(it)) # 1

from itertools import islice
print(list(islice('abcdefghi', 3))) #['a', 'b', 'c']
print(list(islice('abcdefghi', None, 3))) #['a', 'b', 'c']
print(list(islice('abcdefghi', 2, 4))) #['c', 'd']
print(list(islice('abcdefghi', 0, 4, 2))) #['a', 'c']

s = 'he'
t = 'llo'
u = 'hello'

v = s+t
u == v #true

print(id(u)) #1912935944944 #different object in the memory
print(id(v)) #1912948915120

import sys
u = sys.intern('hello')
v = sys.intern(s + t)

print(id(u)) #1253090398960 #the same object in memory
print(id(v)) #1253090398960

# PART 2

import random
random.uniform(1000, 1110)
random.expovariate(1100)
random.expovariate(1 / 5) #if running multiple times the average of the result will be around 5
random.expovariate(5) #if running multiple times the average of the result will be around 0.2

import time
x=10
print(x**2)
print(time.time()) #1696577675.6918454
print(time.ctime()) #Fri Oct  6 10:34:35 2023
time.sleep(5); print('Done') #Done --after some time

import hashlib
print(hashlib.md5('The tale of two cities'.encode('utf-8')))
#  Result: <md5 _hashlib.HASH object @ 0x000002C87FD56D90>
print(hashlib.md5('The tale of two cities'.encode('utf-8')).digest())
# Result: b'\x83S\xb0,<\xd3u\xba\x8d\xa2-\xdd~O"\xfa'
print(hashlib.md5('The tale of two cities'.encode('utf-8')).hexdigest())
# Result: 8353b02c3cd375ba8da22ddd7e4f22fa


print(hashlib.sha1('The tale of two cities'.encode('utf-8')).hexdigest())
# 40d7238a320003ef2f1ab881741792d3735427e6
print(hashlib.sha256('The tale of two cities'.encode('utf-8')).hexdigest())
# b37e58d6cbc67229c3184eeb249899ad0fa0164a27c33b79fffdd14173ab9812
print(hashlib.sha512('The tale of two cities'.encode('utf-8')).hexdigest())
# bbd0129997233fc6aec15b969c98d84fee6573281009caed5870bf97c9a1249b7a5366ba76dfed2578bb881ffef962fdc3fad31359dccceadd323746badd52c9

b = 'The tale of two cities'.encode('utf-8')
b = hashlib.sha512(b).digest()
print(b)

p = 'The tale of two cities'.encode('utf-8')
h = hashlib.pbkdf2_hmac('sha-256', p, b'some phrase', 100000)

# hashlib.pbkdf2_hmac() iterates a sha512 tpo slow-down forward password guessing attacks

s = 'the quick'
t = 'brown fox'

print(s + t) # the quickbrown fox

print(repr((s, t))) # ('the quick', 'brown fox')

los = ['raymond', 'hettiger', 'likes', 'python']

print(' '.join(los)) #raymond hettiger likes python

#Ternary operator = conditional expression

score = 70
print('pass' if score >= 70 else 'fail') #pass

score = 69
print('pass' if score >= 70 else 'fail') #fail

# True and True is always True
# True and False -> False, but in order to say what is it we need to check second one
# meanwhile if there is False and True, we can just skip checking the second one since we know it will be false anyways

3 < 10 and 10 < 20 # true

bool('hello') #true

# 'hello' and  --> True

# True and 'hello' --> 'hello'

def f(x, s= None):
    s=s or 'default'
    print(x, s)

f(10, 'some value') # 10 some value

# Lesson 8: Implementing a Publisher/Subscriber Application (C2, 1.5)

from collections import namedtuple, deque, defaultdict
import time
from typing import NamedTuple, DefaultDict, Optional, List
from pprint import pprint
from itertools import islice
from heapq import merge

Post = namedtuple('Post', ['timestamp', 'user', 'text'])

posts = deque() # Posts from newest to oldest #Type: deque
user_posts = defaultdict(deque) #type: DefaultDict[str, deque]
Timestamp = float # mypy not happy with Optional(float)
def post_message(user: str, text: str, timestamp: Timestamp = None) -> None:
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

# In large programs, emory use is dominated by data not by containers

# from pubsub import * --doesnt work

post_message('guido', 'I love python')

if __name__ == '__main__':
    pprint(posts)
    pprint(user_posts['guido']) #if we want to print only one user's posts
# Result: deque([Post(timestamp=1696579753.6497033, user='guido', text='I love python')])  

# pyflakes 
# mypy

Post = NamedTuple('Post', [('timestamp', str), ('user', str), ('text', str)])

following = defaultdict(set) # type: Dict[User, Set[User]]
followers = defaultdict(set) # type: Dict[User], Set[User]

User = str

def follow(user: User, followed_user: User) -> None:
    following[user].add(followed_user)
    followers[followed_user].add(user)

follow('davin', followed_user='raymondh')
follow('davin', followed_user='guido')

# pprint()

print(len(user_posts['guido']))

from itertools import islice

print(list(islice(user_posts['guido'], None)))

def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(islice(user_posts[user], limit))


if __name__ == '__main__':
    pprint(posts_by_user('guido', limit=1))

user = 'davin'
print(following[user]) # {'raymondh', 'barry'}

for fu in following[user]:
    print(user_posts[fu])

def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(merge(*[user_posts[fu] for fu in following[user]]))

#  It shows newest posts in the beginning

print(list(merge([1,4,9], [2,6,10]))) # [1, 2, 4, 6, 9, 10] asc
print(list(merge([9,4,1], [10,6,1]))) # [9, 4, 1, 10, 6, 1] non sense
print(list(merge([9,4,1], [10,6,1], reverse = True))) # [10, 9, 6, 4, 1, 1]

for followed_user in following[user]:
    print(user_posts[followed_user])

def posts_for_user(user: User, limit: Optional[int]=None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user] 
                       for followed_user in following[user]], reverse = True)
    return list(islice(relevant, limit))

# Interning eliminates redundant strings to save memory

from sys import intern

Post = NamedTuple('Post', [('timestamp', str), ('user', str), ('text', str)])

def post_message(user: str, text: str, timestamp: Timestamp = None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)    

def posts_by_user(user: User, limit: Optional[int]=None) -> List[Post]:
    return list(merge(*[user_posts[fu] for fu in following[user]]))    

def posts_for_user(user: User, limit: Optional[int]=None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user] 
                       for followed_user in following[user]], reverse = True)
    return list(islice(relevant, limit))

for post in posts:
    if 'python' in post.text:
        print(post) # Post(timestamp=1696699514.5952072, user='guido', text='I love python')


def search(phrase: str, limit: Optional[int]= None) -> list[Post]:
    # Todo: add pre-indexing to speed-up searches
    # Todo: Add time sensitive catching
    filtered_posts = [post for post in posts if hasattr(post, 'text') and phrase in post.text]
    return filtered_posts        

if __name__ == '__main__':
    pprint(search('python'))