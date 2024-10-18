F1_PATH = "Lezioni_Enkk\\Lezione_4\\data\\file2_1.txt"
F2_PATH = "Lezioni_Enkk\\Lezione_4\\data\\file2_2.txt"
F3_PATH = "Lezioni_Enkk\\Lezione_4\\data\\file2_3.txt"


with open(F1_PATH, "r") as f:
	lines_file_1 = [word.strip("\n") for word in f.readlines()]

with open(F2_PATH, "r") as f:
	lines_file_2 = [word.strip("\n") for word in f.readlines()]

list_3 = [line for line in lines_file_1 if line in lines_file_2]
list_3.reverse()

#with open('F3_PATH', 'w') as f3:
#    f3.writelines(list_3)

with open(F3_PATH, 'w') as f:
    for line in list_3:
        f.write(line)
        f.write('\n')