import random as r

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

def matrix_copy(sigmas: list[list[float]]) -> list[list[float]]:
	copy: list[list[float]] = []
	for i in range(len(sigmas)):
		copy.append(sigmas[i].copy())
	return copy

def calculate_determinant(matrix: list[list[float]]) -> float:
	dimension: int = len(matrix)
	sigmas: list[list[float]] = all_sigmas([i for i in range(dimension)])
	signs: list[int] = find_sign(matrix_copy(sigmas))
	total_result: float = 0
	for i in range(len(sigmas)):
		curr: float = 1
		for row, col in enumerate(sigmas[i]):
			curr *= matrix[row][col]
		total_result += curr * signs[i]
	return total_result

def generate_matrix(n: int) -> list[list[float]]:
	matrix: list[list[float]] = []
	for i in range(n):
		matrix.append([r.randint(-100, 100) for _ in range(n)])
	return matrix

def display_matrix(matrix: list[list[float]]) -> None:
	copied = matrix_copy(matrix)
	for line in copied:
		print(" ".join(map(str, line)))


n = int(input("What size should the matrix be? "))
matrix: list[list[float]] = generate_matrix(n)
print(f"You generated the following matrix {n}x{n}:")
display_matrix(matrix)
det: float = calculate_determinant(matrix)
print(f"The determinant is: {det}")
print("Approximation: %.3g" %det)