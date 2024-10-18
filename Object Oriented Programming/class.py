row1 = ["|"," ", "|"," ", "|"," ", "|"]
row2 = ["|"," ", "|"," ", "|"," ", "|"]
row3 = ["|"," ", "|"," ", "|"," ", "|"]

board = row1 + row2 + row3

row_1 = " ".join(row1)
row_2 = " ".join(row2)
row_3 = " ".join(row3)

board_ = [row_1,  row_2,  row_3]

board_display = "\n".join(board_)
print(board_display)