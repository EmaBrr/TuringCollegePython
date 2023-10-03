# name = input('Enter your name: ')
# print(f'Hello, {name}!')

def pig_latin():
    en_word = input('Enter english word: ')

    if en_word.isalpha():
        
        letters = [letter for letter in en_word] # Split word into letters
        if letters[0].upper() in ('A', 'E', 'I', 'O', 'U'): # Checks if word starts with these letters
            new_end = 'way'
            new_word = ''.join([en_word, new_end])
        else:
            letters = []
            for letter in en_word[1:]: # Spliting the word into letters without first letter
                letters.append(letter) 
            
            new_end = 'ay'
            en_word_without_start = ''.join(letters)
            new_word = ''.join([en_word_without_start, en_word[0], new_end])
           
        print(f'New word in pig latin is: {new_word}')

    else:
        print("Input is not a string.")   

pig_latin()    


# CHATGPT suggestion of how to improve the code:

# def pig_latin():
#     """
#     Converts an English word to Pig Latin.
#     """
#     en_word = input('Enter an English word: ').strip()  # Strip whitespace from input

#     if en_word.isalpha():
#         en_word_lower = en_word.lower()  # Convert to lowercase for case-insensitive vowel check
#         if en_word_lower[0] in ('a', 'e', 'i', 'o', 'u'):
#             new_word = f'{en_word}way'
#         else:
#             en_word_without_start = en_word[1:]
#             new_word = f'{en_word_without_start}{en_word[0]}ay'

#         print(f'New word in Pig Latin is: {new_word}')
#     else:
#         print("Input is not a string.")

# pig_latin()


# Exercise in HackerRank

from collections import deque

def deque_f():
    try:
        action_count = int(input("How many actions you want to do with deque: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit(1)
    
    my_deque = deque()

    for i in range(action_count):
        action = input("Action that you want to do with deque: ")
        words = action.split()
        action_on_deque = words[0]

        if len(words) == 2:
            number = words[1] 
        
            if action_on_deque.lower() == 'append':
                my_deque.append(number)
            elif action_on_deque.lower() == 'appendleft':
                my_deque.appendleft(number)

        elif len(words) == 1 and len(my_deque) != 0 :
            if action_on_deque.lower() == 'pop':
                my_deque.pop()
            elif action_on_deque.lower() == 'popleft':   
                my_deque.popleft()
        else:
            'Input is incorrect'
    elements_as_string = ' '.join(map(str, my_deque))
    print(elements_as_string)


deque_f()   

