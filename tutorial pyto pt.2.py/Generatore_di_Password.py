import random
import string
def password_gen():
	alfanum = string.ascii_letters + string.digits
	ascii_all = alfanum + string.punctuation
	diff = input("vuoi una password (c) complicata o (s) semplice? ")
	x = 0
	password = ""
	if diff == "s":
		while x < 8:
			password += random.choice(alfanum)
			x += 1
	elif diff == "c":
		while x < 20:
			password += random.choice(ascii_all)
			x += 1
	else:
		print("invalid imput")
	
	return password

print(password_gen())