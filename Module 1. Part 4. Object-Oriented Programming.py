# Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.

# How Do You Define a Class in Python?

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Why we need objects? Let's say we need to track info about employees, so we could create a list. 

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# However, if let's say year is missing, then with mccoy[1] we would get his position and not year as it would be for others.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

