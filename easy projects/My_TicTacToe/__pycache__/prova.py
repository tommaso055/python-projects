def player_won(letter, board):
    result = False

    # checking rows
    for row in board:
        if row.count(letter) == 3:
            result = True

    # checking columns
    for column in range(3):
        col_letters = []
        for row in board: 
            col_letters.append(row[column])
        if col_letters.count(letter) == 3:
            result = True

    # checking diagonals
    i = 0
    diag_letters = []
    for row in board: 
        diag_letters.append(row[i])
        i += 1
    if diag_letters.count(letter) == 3:
        result = True

    i = -1
    diag_letters = []
    for row in board: 
        diag_letters.append(row[i])
        i -= 1
    if diag_letters.count(letter) == 3:
        result = True

    return result

player_won(letter, board)