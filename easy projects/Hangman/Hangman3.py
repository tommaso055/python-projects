import random
from lista_ita import lista
import string
def valid_word():
	word = random.choice(lista)
	while "-" in word or " " in word:
		word = random.choice(lista)
	return word.upper()
def hangman():
	secret_word = valid_word()
	word_letters = set(secret_word)
	alphabet = set(string.ascii_uppercase)
	used_letters = set()
	
	lives = 6
	
	while len(word_letters) > 0 and lives > 0:
		
		print(f"You have {lives} lives")

		print("Letters you have used: ", " ".join(used_letters))
		
		word_list = [letter if letter in used_letters else "-" for letter in secret_word]
		print("Current word: ", " ".join(word_list))

		guess = input("\nEnter a letter: ").upper()
		if guess in alphabet and not guess in used_letters:
			used_letters.add(guess)
			if guess in secret_word:
				word_letters.remove(guess)
			else:
				lives -= 1
				print(f"the letter {guess} in not in the secret word")
		elif guess in used_letters:
			print("you have already used this letter")
		else:
			print("invalid input")
	print(secret_word) 
hangman()