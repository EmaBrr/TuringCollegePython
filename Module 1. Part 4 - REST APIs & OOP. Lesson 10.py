# Lesson 10: Building a Web Application for the PubSub Service (C2, 1)

# Copy of Lesson 8: Implementing a Publisher/Subscriber Application (C2, 1.5)

from collections import namedtuple, deque, defaultdict
import time
from typing import NamedTuple, DefaultDict, Optional, List
from pprint import pprint
from itertools import islice
from heapq import merge
from sys import intern
from bottle import route, run, post, view, response, request, static_file, template
import pubsub as comb
import session

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', str), ('user', str), ('text', str)])
posts = deque() # Posts from newest to oldest #Type: deque
user_posts = defaultdict(deque) #type: DefaultDict[str, deque]
following = defaultdict(set) # Type: Dict[User, Set[User]]
followers = defaultdict(set) # Type: Dict[User], Set[User]

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

# Publisher/Subcriber Service
# * Display login page and check credentials
# * Show main page
# * Run search
# * Post a message
# * Display followers or following
# * Show user page
# * Return static content

secret = 'The life expentancy of a lannister stark or targaryen is short'

@route('/')
@view('main.tpl')
def show_main_page(user=None, posts= [], phrase=''):
    if user is None:
        user = request.get_cookie('user', secret = secret)
    if user is None:
        return template('login.tpl', null=None)
    heading = 'Posts from people you follow'
    posts = pubsub.posts_for_user(user)
    return dict(user=user, posts=posts, heading=heading, comb=comb)

@post('/')
def check_credentials():
    user = request.forms.get('user', '')
    password = request.forms.get('password', '')
    if not pubsub.check_user(user, password):
        time.sleep(1)
        # XXX Add failed message and increment failure counter
        return show_main_page()
    response.set_cookie('user', user, max_age = 600, secret=secret) # 600 seconds customers will be logged in
    return show_main_page(user)

@post('/postmessage')
def post_message():
    loggedin_user = 'davin'
    text = request.forms.get('text', '')
    if text:
        pubsub.post_message(loggedin_user, text)
    return show_main_page

@route('/search')
@view('main.tpl')
def show_search():
    loggedin_user = 'davin'
    phrase = request.query.get('phrase', '')
    posts = []
    if phrase:
        posts= pubsub.search(phrase, limit = 10)
    heading = 'Posts maching: %s' % phrase
    return dict(user= loggedin_user, posts = posts, heading=heading, comb=comb)

@route('/<user>')
@view('user.tpl')
def show_user_page(user):
    return dict(user = user, posts= pubsub.user_posts[user], heading = 'Recent posts', comb=comb)

@route('/<user>/followers')
@view('follow.tpl')
def show_followers(user):
    return dict(
        users = pubsub.followers[user], 
        who_does_what = 'Who follows %s' % user, 
        comb = comb,
    )

@route('/<user>/following')
@view('follow.tpl')
def show_following(user):
    return dict(
        users = pubsub.following[user], 
        who_does_what = 'Who %s is following' % user, 
        comb = comb,
    )

@route('/static/<filename>')
def fetch_static(filename):
    response.set_header('Cache-Control', 'max-age= 600')
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', post=8080)