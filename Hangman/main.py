import random
from functions import letter_input
from functions import category_input
from functions import print_hangman
from functions import letter_in_word
from functions import is_in_word
from functions import winner
from functions import random_choice_from_category


# with open('your_file.txt', 'r') as file:
#     file_content = file.read()
#     words_list = file_content.split()
#     random_word = random.choice(words_list)

# print(random_word)
letters = []
word_pakac = ''
false_letter = 0


name = input('Enter your name: ')
chosen_category = category_input()
chosen_word = random_choice_from_category(chosen_category)




for i in range(len(chosen_word)):
    word_pakac += '-'

while not(winner(word_pakac)):
    print(word_pakac)
    letter = letter_input(name, letters)
    letters.append(letter)
    if is_in_word(letter, chosen_word):
        word_pakac = letter_in_word(chosen_word, letter, word_pakac)
    else:
        false_letter += 1
        print_hangman(false_letter)


print(chosen_word)
