from functions import printboard
from functions import winner
from functions import is_empty
from functions import validation
from functions import validation2


name1 = input('Enter player1 name: ')
name2 = input('Enter player2 name: ')

victory1 = 0
victory2 = 0
batches = 1
play_again = 'yes'

while play_again == 'yes':
    board = [' ',  ' ',  ' ',  ' ',  ' ',   ' ',  ' ',  ' ',   ' ']
    printboard(board)
    for i in range(9):
        if i % 2 == 0:
            while True:
                choice1 = validation(name1)
                if is_empty(board, choice1):
                    board[choice1 - 1] = 'X'
                    break
                print('Please enter a number, which is empty')
            printboard(board)
            if winner(board):
                victory1 += 1
                print(f'{name1} won!!!')
                break  # Exit the loop if there's a winner
        if i % 2 == 1:
            while True:
                choice2 = validation(name2)
                if is_empty(board, choice2):
                    board[choice2 - 1] = 'O'
                    break
                print('Please enter a number, which is empty')
            printboard(board)
            if winner(board):
                victory2 += 1
                print(f'{name2} won!!!')
                break # Exit the loop if there's a winner
        if i == 8:
            print('Nichya')

    while True:
        play_again = input("Do you wanna play again? [yes/no]։ \n ")
        if validation2(play_again):
            break
        print("Please enter 'yes' or 'no'")
    if play_again == "no": 
         print("Are you leaving already? How sad :("
            "\nOkay, let's look at the statistics then"
            f"Total batches: {batches}"
            f"Amount of winnings:\n{name1}: {victory1}\n{name2}: {victory2}")
    else: 
       batches += 1