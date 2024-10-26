import random
from data import words
import string
def valid_word():
	word = random.choice(words)
	while "-" in word or " " in word:
		word = random.choice(words)
	return word.upper()
def hangman():
	secret_word = valid_word()
	word_letters = set(secret_word)
	showed_word = "-" * len(secret_word)
	alphabet = set(string.ascii_uppercase)
	used_letters = set()
	lives = 6
	while showed_word != secret_word:
		print(f"Letters you have used: {used_letters}")
		print(showed_word)
		guess = input("\nEnter a letter: ").uppercase()
		if guess in alphabet and not guess in used_letters:
			used_letters.add(guess)
			if guess in secret_word:
				word_letters.remove(guess)
			else:
				life -= 1
		elif guess in used_letters:
			print("you have already used this letter")
		else:
			print("invalid input")


	
	    


hangman()