import random

def used_letter(letter, letters):
    if letter in letters:
        return True
    return False


def letter_input(name, letters):
    ''' stugum a usery tar a nermucel, te che '''
    while True:
        entered_letter = input("Enter a letter: ")
        if entered_letter.isalpha() and len(entered_letter) == 1:
            while True:
                if not(used_letter(entered_letter, letters)):
                    return entered_letter
                print('Please enter a new letter')
                entered_letter = input("Enter a letter: ")
        print(f"{name} please be more careful:)\nYour input is not a letter. Try again: ")
        



def category_input():
    ''' sturgum a usery goyutyun unecox category a ynter, te che '''
    print("Choose a category\n--------CATEGORIES--------\n\n\t\t1. Animals",
          "\n\t\t2. Professions\n\t\t3. Countries and Cities",
          "\n\t\t4. Fruits and Vegetables\n")   
    while True:
        choose_category = input("Choose the category: ")
        if choose_category == '1' or choose_category == '2' or choose_category == '3' or choose_category == '4':
            return choose_category
            
        print("No such category exists. Please, try once more: \n")


def print_hangman(false_letter):
    ''' nkarum a mardukin sxal nermucac tareri qanakin hamapatasxan vichakum '''
    if false_letter == 1:    
        print("\n|\n|\n|\n|\n|")
    elif false_letter == 2:
        print(" \n---------\n|\n|\n|\n|\n|")
    elif false_letter == 3:
        print(" \n---------\n|\t\t|\n|\n|\n|\n|")
    elif false_letter == 4:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\n|\n|")
    elif false_letter == 5:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t\t| \n|\n|")
    elif false_letter == 6:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t       /| \n|\n|")
    elif false_letter == 7:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t       /|\ \n|\n|")
    elif false_letter == 8:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t       /|\ \n|\t      / \n|")
    elif false_letter == 9:
        print("\n---------\n|\t|\n|\tO\n|      /|\ \n|      / \ \n|", "\nYOU LOSE:(")
    print('\n')
    
    
def letter_in_word(chosen_word, letter, word_pakac):
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            word_pakac = word_pakac[:i] + letter + word_pakac[i + 1:]
    return word_pakac



def is_in_word(letter, chosen_word):
    if letter in chosen_word:
        return True
    return False

def winner(word_pakac):
    if '-' in word_pakac:
        return False
    return True




def random_choice_from_category(choosen_category):
    """ This function selects a random word from the appropriate category """
    
    if choosen_category == "1":
        with open('Animals.txt', 'r') as file:
            text = file.read()
            words = text.split()
            random_animal = random.choice(words).lower()

            if words:
                return random_animal

    if choosen_category == "2":  # Use elif instead of another if
        with open('Professions.txt', 'r') as file:
            text = file.read()
            words = text.split()
            random_profession = random.choice(words).lower()

            if words:
                return random_profession

    if choosen_category == "3":
        with open('Countries_cities.txt', 'r') as file:
            text = file.read()
            words = text.split()
            random_country_or_city = random.choice(words).lower()

            if words:
                return random_country_or_city

    if choosen_category == "4":
        with open('Fruits_Vegetables.txt', 'r') as file:
            text = file.read()
            words = text.split()
            random_fruit_or_vegetable = random.choice(words).lower()

            if words:
                return random_fruit_or_vegetable
