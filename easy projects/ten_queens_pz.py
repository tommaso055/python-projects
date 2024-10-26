def check_valid(n, ls):
	l = len(ls)
	if n in ls: return False
	for i in range(l):
		if ls[i] == n - i - 1 or ls[i] == n + i + 1:
			return False
	return True

def find_all_combs(width, length):
	
	if not length: raise ValueError
	if width == 1: return [[i] for i in range(length)]

	rightside_combs = find_all_combs(width - 1, length)

	all_combs = []
	for leftmost_column_square in range(length):
		for rightside_comb in rightside_combs:
			if check_valid(leftmost_column_square, rightside_comb):
				all_combs.append([leftmost_column_square] + rightside_comb)

	return all_combs

for comb in find_all_combs(10, 10):
	comb = map(str, comb)
	print("".join(comb))