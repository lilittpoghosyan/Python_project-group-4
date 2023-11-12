import random
from functions import letter_input
from functions import category_input
from functions import print_hangman
from functions import letter_in_word
from functions import is_in_word
from functions import winner




with open('your_file.txt', 'r') as file:
    file_content = file.read()
    words_list = file_content.split()
    random_word = random.choice(words_list)

print(random_word)


name = input('Enter your name: ')
letters = []
words = ['banana', 'avakada', 'manga', 'apple']

chosen_word = random.choice(words)
print(chosen_word)

word_pakac = ''
false_letter = 0


for i in range(len(chosen_word)):
    word_pakac += '-'

while not(winner(word_pakac)):
    letter = letter_input(name, letters)
    letters.append(letter)
    if is_in_word(letter, chosen_word):
        word_pakac = letter_in_word(chosen_word, letter, word_pakac)
    else:
        false_letter += 1
        print_hangman(false_letter)

    print(word_pakac)

