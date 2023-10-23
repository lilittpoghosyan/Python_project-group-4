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
        if board[i] == board[i + 1] == board[i + 2] == 'X' or 'O':
            return board[i]
        else:
            False

    """
    This is going to check the columns
    """

    for j in range(0, 3, 1):
        if board[j] == board[j + 3] == board[j + 6] == X or O:
            return board[j]
        else:
            False

    """
    These two are going to check the diagonals
    """

    if board[0] == board[4] == board[8] == 'X' or 'O':
        return board[0]
    else:
        False

    if board[2] == board[4] == board[6] == 'X' or 'O':
        return board[2]
    else:
        False

def inputt():
    while True:
        n = input("Choose the case: \n")
        if n.isdigit() and int(n) >= 1 and int(n) < 10:
            break 
        else: 
            print("!!!Please enter the number between 1 and 9")
    while True: 
        b = input("Enter your symbol: [x / o]\n")
        if b == "x" or b == "o":
            board[int(n) - 1] = b
            break
        else: 
            print("!!!Unidentified character. Please enter x or o: ")
    



board = [' ',  ' ',  ' ',  ' ',  ' ',   ' ',  ' ',  ' ',   ' ']
printboard(board)
