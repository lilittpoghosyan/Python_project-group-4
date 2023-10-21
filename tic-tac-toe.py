def winner(table):
    """
    This is going to check the rows
    """
    for i in range(0, 9, 3):
        if table[i] == table[i + 1] == table[i + 2] == X or O:
            return table[i]
        else:
            False

    """
    This is going to check the columns
    """

    for j in range(0, 3, 1):
        if table[j] == table[j + 3] == table[j + 6] == X or O:
            return table[j]
        else:
            False

    """
    These two are going to check the diagonals
    """

    if table[0] == table[4] == table[8] == X or O:
        return table[0]
    else:
        False

    if table[2] == table[4] == table[6] == X or O:
        return table[2]
    else:
        False

