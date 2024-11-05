
def all_sigmas(elements: list[int]) -> list[list[int]]:
	if (len(elements) < 2): return [elements]
	result: list[list[int]] = []
	for i in range(len(elements)):
		result += [[elements[i]] + sigma for sigma in all_sigmas(elements[:i] + elements[i + 1:])]
	return result


def find_sign(sigmas: list[list[int]]) -> list[int]:
	n: int = len(sigmas[0])
	signs: list[int] = []
	for sigma in sigmas:
		count = 0
		for i in range(n):
			for j in range(i, n):
				if sigma[j] == i and i != j:
					sigma[j] = sigma[i]
					sigma[i] = i
					count += 1
		if count % 2:
			signs.append(-1)
		else:
			signs.append(1)
	return signs

def s_copy(sigmas: list[list[int]]) -> list[list[int]]:
	copy: list[list[int]] = []
	for i in range(len(sigmas)):
		copy.append(sigmas[i].copy())
	return copy

def calculate_determinant(matrix: list[list[float]]) -> float:
	dimension: int = len(matrix)
	sigmas: list[list[int]] = all_sigmas([i for i in range(dimension)])
	signs: list[int] = find_sign(s_copy(sigmas))
	total_result: float = 0
	for i in range(len(sigmas)):
		curr: float = 1
		for row, col in enumerate(sigmas[i]):
			curr *= matrix[row][col]
		total_result += curr * signs[i]
	return total_result

matrix1 = [
[5, 7, 2],
[4, -2, 5],
[2, -1, -6]
]

matrix2 = [
[5, 7, 2, 3],
[4, -2, 5, 8],
[2, -1, -6, 4],
[6, 6, 12, 9],
]

print(calculate_determinant(matrix2))