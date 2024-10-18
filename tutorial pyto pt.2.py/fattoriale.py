def fattoriale(num):
	if num > 0:
		return fattoriale(num-1)*num
	else:
		return 1