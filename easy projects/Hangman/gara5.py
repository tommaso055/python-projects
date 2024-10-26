import math
pi = 3.14159265359
valid = True
lati = 10

while valid:
	lilangle = pi/(2*lati)
	angle = (180*(lati-2))/lati
	diag = 1

	for _ in range(lati//2 - 1):
		diag = math.sqrt(diag**2 + 1 - 2*(diag*math.cos(angle)))
		angle += lilangle

	last = diag
	if diag > 2023:
		valid = False
print(last)





