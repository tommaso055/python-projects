import random
def rock_paper_scissors():
	moves = {
	"r":"rock",
	"p":"paper",
	"s":"scissors",
	}
	while True:
		user = input("\nWrite r for playing rock, p for playing paper and s for playing scissors: ")
		computer = random.choice(["r","p","s"])
		print(f"I did pick {moves[computer]}")
		#cases
		a = user == "r" and computer == "p"
		b = user == "p" and computer == "s"
		c = user == "s" and computer == "r"
		d = user == "r" and computer == "s"
		e = user == "s" and computer == "p"
		f = user == "p" and computer == "r"
		
		if user == computer:
			print("We're even")
		elif a or b or c:
			print("Haha you lost")
		elif d or e or f:
			print("Rip you won")
		elif user == "stop":
			break
		else:
			print("invalid input")

rock_paper_scissors()
