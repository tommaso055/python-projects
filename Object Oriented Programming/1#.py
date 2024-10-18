class GuessNumber:
	def __init__(self, number, min, max):
		self.number = number
		self.guesses = 0
		self.min = min
		self.max = max
	
	def get_guess(self):
		guess = input(f"Guess a number between {self.min} and {self.max}: ")

		if self.valid_number(guess):
			return int(guess)
		else:
			print("Enter a valid number: ")
			return self.get_guess()

	def valid_number(self, str_number):
		try:
			number = int(str_number)
		except:
			return False

		return self.min <= number <= self.max

	def play(self):
		while True:
			self.guesses += 1

			guess = self.get_guess()
			if guess < self.number:
				print("Try higher...")
			elif guess > self.number:
				print("Try lower...")
			else:
				print("congrats, you won!")
				break


game = GuessNumber(63,1,100)
game.play()