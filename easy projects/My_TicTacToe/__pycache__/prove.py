board = [[1,2,3],[4,5,6],[7,8,9]]
print(board)
while True:
    n = int(input())
    row = n // 3 
    column = n % 3 
    board[row][column] = "X"
    print(board)
