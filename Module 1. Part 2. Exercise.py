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