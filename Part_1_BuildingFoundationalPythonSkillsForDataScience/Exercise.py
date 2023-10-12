# https://www.hackerrank.com/dashboard

python_students = [['Prashant', 32], ['Pallavi', 36], ['Dheeraj', 39], ['Shivam', 40]]

belekas = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input());
        belekas.append([name,score])

        
from collections import Counter 

second_elements = sorted(Counter([list[1] for list in belekas]))

items_with_second_biggest_value = []
for record in belekas:
    if record[1] == second_elements[1]:
        items_with_second_biggest_value.append(record[0])

for item in sorted(items_with_second_biggest_value):
    print(item)


# Number guessing game

# 1 Numeric types | Exercise 1 ■ Number guessing game
# This first exercise introduces a number of topics that will repeat themselves over your Python career: loops, user input, converting types, and comparing values.
# More specifically, programs all have to get input to do something interesting, and that input often comes from the user. Knowing how to ask the user for input 
# not only is useful, but allows us to think about the type of data we’re getting, how to convert it into a format we can use, and what the format would be.
# As you might know, Python only provides two kinds of loops: for and while. Knowing how to write and use them will serve you well throughout your Python career.
# The fact that nearly every type of data knows how to work inside of a for loop makes such loops common and useful. If you're working with database records, elements in an XML file, 
# or the results from searching for text using regular expressions, you'll be using for loops quite a bit.

# Write a function (guessing_game) that takes no arguments.
# When run, the function chooses a random integer between 0 and 100 (inclusive).
# Then ask the user to guess what number has been chosen.
# Each time the user enters a guess, the program indicates one of the following:
# Too high
# Too low
# Just right
# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
# The program only exits after the user guesses correctly.
# We’ll also be prompting the user to enter text with the input function. We’ll actually be using input quite a bit in this book to ask the user to tell us something. 
# The function takes a single string as an argument, which is displayed to the user. The function then returns the string containing whatever the user entered; for example:

name = input('Enter your name: ')
print(f'Hello, {name}!')
# If the user simply presses Enter when presented with the input prompt, the value returned by input is an empty string, not None. 
# Indeed, the return value from input will always be a string, regardless of what the user entered.     

import random

def guessing_game():
    result = random.randint(0, 100) 
    print(result)

    def inner_function():
        print('Guess the number between 0 and 100:')
        try:
            x = int(input())
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            inner_function()
            return
        
        if x == result:
            print('Congratulations, you are correct!')
        elif x > result:
            print('A bit too high, try again.')
            inner_function()
        elif x < result:
            print('A bit too low, try again.')
            inner_function()

    inner_function()

guessing_game()