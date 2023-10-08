# Lesson 9: Using Bottle to Build REST APIs and Web Applications (C2, 1)

# Bottle, another one is Flask or Django

# Big idea:
# Micro-webframeworks (such as Bottle) are all about minimizing the code and effort required to links an application to a web server. Decorators connect a route or path to a function. The function manages getting a user request, calling the application and forming the response.response

from bottle import * 
from pprint import pprint
import time
import math
# import algebra # Doesn't work

print(time.time()) # 1696758220.0046105


# We will use a decorator to attach a route or path 
@route('/') # http://localhost:8080
def welcome():
    # Pridėjome in Lesson 2, po JSON:
    response.set_header('Vary', 'Accept')
    # pprint(dict(request.headers)) # This is debugging line
    # How to do content negotiation attempts to honor user preferences:
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy </h1>'
    response.content_type = 'text/plain'
    return 'Hello'

@route('/now') # http://localhost:8080/now
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age = 1')
    return time.ctime()

@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()

# @route('/area/circle')
# def circle_area_service():
#     print(dict(request.query))
#     return 'Test'
#     # return math.pi * radius ** 2.0

# Question: where to write: curl 'http://localhost:8080/'?
# How to do content negotiation attempts to honor user preferences:

# Part 2
secret = 'the average life expectance of shark or tangaryan is short'

@route('/area/circle')
def circle_area_service():
    # Pridėjome in Lesson 2, po JSON:
    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    print(f'Last visit {last_visit}')
    response.set_cookie('last-visit', time.ctime()) # Printing when the last visit was
    response.set_header('Vary', 'Accept')
    pprint(dict(request.query))
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0] # jis šitą sugalvojo, kai paleido su xyz, tai nukopino iš error kur gavo: could not convert string to float: xyz
    # area = algebra.area_circle(radius) #Reikia importinti algebra
    # if 'text/html' in request.headers.get('Accept', '*/*'):
    #     response.content_type = 'text/html'
    #     # return f'<p> The area is <em> {area}</em> </p>'
    # return 'Test: %r' % radius
    return dict(radius=radius, service = request.path)

# Paleidžiam va taip: http://localhost:8080/area/circle?radius=10
# Paleidžiam va taip: http://localhost:8080/area/circle?radius=xyz
# Jeigu paleistume radius=xyz tai tada gautųme error 500 - server errors indicate a need for better error handling

# JASON - JavaScrip Object Notation
# REST APIs typically return JSON objects

# Content negotiation can confuse caches unless the "Vary" head is used

from bottle import template
print(template('The answer is {{x}} today', x=10))
print(template('The answer is {{x**2}} today', x=10))

lastname = 'hettinger'
first_names = 'raymond rachel matthew'.split()
family_template = '''The {{lastname.title()}} Family 
{{'='*(len(lastname)+11)}}
% for name in first_names:
*    {{name.title()}}
% end'''

print(template(family_template, lastname=lastname, first_names=first_names))

# The Hettinger Family
# ====================
# *    Raymond
# *    Rachel
# *    Matthew

import os
os.listdir('Congress_data') # ką čia reikėtų rašyti? congress_votes neveikia

## File Server ##########################

file_template = '''\
<h1> List of files in <em> Congress data </em> directory </h1>
<hr>
<ol>
    % for file in files:
    <li> <a href={{file}}>{{file}} </li>
    % end
</ol>
'''
@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir('Congress_data')
    if 'text/html' not in request.headers.get('Accept', '*/*'):
        return dict(files=files)
    return(template(file_template, files=files))

@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, './Congress_data')

# http://localhost:8080/files/congress_votes_118-2023_s247.csv download this file

# Šitas visada turi būti gale
if __name__ == '__main__':
    run(host='localhost', port = 8080)



