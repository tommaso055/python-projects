import random
def computer_guess(x):
	bot = 1
	top = x
	response = ""
	guess = 0
	while True:
		guess = random.randint(bot,top)
		print(f"Is your number {guess}?")
		response = input()
		if response == "no":
			response = input("Is it higher or lower? ")
			if response == "higher":
				bot = guess + 1
			if response == "lower":
				top = guess - 1
		elif response == "yes":
			break
		else:
			print("just answer yes or no")
	print("haha, i'm too strong")

computer_guess(100)