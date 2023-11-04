def printboard(board):
    print(' ----- ----- -----')
    print('|     |     |     |')
    print(f'|  {board[0]}  |  {board[1]}  |  {board[2]}  |')
    print('|     |     |     |')
    print(' ----- ----- -----')
    print('|     |     |     |')
    print(f'|  {board[3]}  |  {board[4]}  |  {board[5]}  |')
    print('|     |     |     |')
    print(' ----- ----- -----')
    print('|     |     |     |')
    print(f'|  {board[6]}  |  {board[7]}  |  {board[8]}  |')
    print('|     |     |     |')
    print(' ----- ----- -----')



def winner(board):
    """
    This is going to check the rows
    """
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] and board[i] == board[i + 2] and not(board[i] == ' '):
            return True

    """
    This is going to check the columns
    """

    for j in range(0, 3, 1):
        if board[j] == board[j + 3] and board[j] == board[j + 6] and not(board[j] == ' '):
            return True
    """
    These two are going to check the diagonals
    """

    if board[0] == board[4] and board[0] ==  board[8] and not(board[0] == ' '):
            return True

    if board[2] == board[4] and board[2] == board[6] and not(board[2] == ' '):
            return True
    return False


def validation(name):
    while True:
        n = input(f"{name}'s turn: ")
        if n.isdigit() and int(n) >= 1 and int(n) < 10:
            return int(n)
        print("!!!Please enter the number between 1 and 9")
    
def is_empty(board, choice):
    if board[choice - 1] == ' ':
        return True
    return False

def validation2(play_again):
    if play_again == 'yes' or play_again == 'no':
        return True
    return False