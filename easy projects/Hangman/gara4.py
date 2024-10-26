fact = 1
tot = 0
for i in range(1, 2024):
	fact = fact*i
	n = len(str(fact))
	tot+=n
print (tot)


