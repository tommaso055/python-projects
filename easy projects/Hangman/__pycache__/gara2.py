count = 0
for a in range(1, 10):
	for b in range (0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				if a+b+c+d == a*b*c*d:
					count+=1
print(count)