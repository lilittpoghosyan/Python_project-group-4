def letter_validation(name):
    ''' stugum a usery tar a nermucel, te che '''
    while True:
        entered_letter = input("Guess the letter: ")
        if  entered_letter.isalpha() and len(entered_letter) == 1:
            return entered_letter
            break
        else:
            print(f"{name} please be more careful:)\nYour input is not a letter. Try again: ")
        

def category_validation():
    ''' sturgum a usery goyutyun unecox category a ynter, te che '''
    print("--------CATEGORIES--------\n\n\t\t1. Animals",
          "\n\t\t2. Professions\n\t\t3. Countries and Cities",
          "\n\t\t4. Fruits and Vegetables\n")   
    while True:
        choose_category = input("Choose the category: ")
        if choose_category == '1' or choose_category == '2' or choose_category == '3' or choose_category == '4':
            return choose_category
            
        else:
            print("No such category exists. Please, try once more: \n")


def picture(false_letter):
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
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t   /| \n|\n|")
    elif false_letter == 7:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t   /|\ \n|\n|")
    elif false_letter == 8:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t   /|\ \n|\t   / \n|")
    elif false_letter == 9:
        print(" \n---------\n|\t\t|\n|\t\tO\n|\t   /|\ \n|\t   / \ \n|", "\nYOU LOSE:(")
    
    
