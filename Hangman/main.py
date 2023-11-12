import random
from functions import letter_input
from functions import category_input
from functions import print_hangman
from functions import letter_in_word
from functions import is_in_word
from functions import winner




# with open('your_file.txt', 'r') as file:
#     file_content = file.read()
#     words_list = file_content.split()
#     random_word = random.choice(words_list)

# print(random_word)


name = input('Enter your name: ')
letters = []
animal_names = [
    "lion", "elephant", "giraffe", "zebra", "tiger", "kangaroo", "penguin", "cheetah",
    "koala", "panda", "rhino", "hippo", "lemur", "otter", "jaguar", "parrot", "snake",
    "crocodile", "dolphin", "whale", "octopus", "gazelle", "buffalo", "fox", "bear",
    "wolf", "bat", "seagull", "mongoose", "dingo", "platypus", "cockatoo", "skunk",
    "armadillo", "lemming", "quokka", "vulture", "wombat", "lynx", "hamster", "kookaburra",
    "chameleon", "frog", "pangolin", "panther", "lemur", "armadillo", "iguana", "lemming",
    "numbat", "tapir", "ocelot", "reindeer", "bobcat", "sloth", "cockroach", "chinchilla",
    "impala", "yak", "gecko", "salamander", "macaw", "wallaby", "stoat", "hedgehog",
    "narwhal", "kookaburra", "woodpecker", "humpback", "quokka", "vulture", "shrimp",
    "toucan", "wolverine", "barracuda", "armadillo", "weasel", "lynx", "mongoose", "axolotl",
    "chimpanzee", "orangutan", "lemur", "gibbon", "gorilla", "bonobo", "baboon", "macaque",
    "capuchin", "tamarin", "siamang", "howler", "spider", "platypus", "giraffe", "gorilla"
]

chosen_word = random.choice(animal_names)

word_pakac = ''
false_letter = 0


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



