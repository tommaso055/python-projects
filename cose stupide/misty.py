def misty(n):
	sum_value = 0
	i = 0
	for i in range(n):
		sum_value += i / (2**(i + 1))
	return sum_value

print(misty(1000))