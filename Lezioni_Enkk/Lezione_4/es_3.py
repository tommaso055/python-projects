url_1 = "Lezioni_Enkk\\Lezione_4\\data\\file3_1.txt"
url_2 = "Lezioni_Enkk\\Lezione_4\\data\\file3_2.txt"

def list_to_matrix(url_file):
	with open(url_file, "r") as f:
		lines = [word.strip("\n") for word in f.readlines()]
	l1 = list(lines[0])
	l2 = list(lines[1])

	while "," in l1:
		l1.remove(",")

	while "," in l2:
		l2.remove(",")

	l_1 = list(map(int, l1))
	l_2 = list(map(int, l2))
	
	diagonal = [l_1[row] + l_2[row] for row in range(len(l_1))]

	with open(url_2, "w") as f:
		for item in diagonal:
			f.write(str("0 "*diagonal.index(item)))
			f.write(str(item) + " ")
			f.write(str("0 "*(len(diagonal) - diagonal.index(item) - 1)).strip())
			f.write("\n")

list_to_matrix(url_1)