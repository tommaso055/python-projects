import random
from data import words

def hangman():
	lives = 6
	secret_word = random.choice(words)
	print("Hi, welcome to the hangman game, you will need to guess the secret word. You can try to guess the whole word or just a letter, but after 5 mistakes, you're out! \nLet's start!")
	print(f"\nThe secret word is long {len(secret_word)} letters.")
	while lives > 0:
		guess = input("\nEnter your guess: ")
		if len(guess) == 1:
			if guess in secret_word:
				print(f"Yes!the letter {guess} is part of the secret word!")
				k = 0
				for letter in secret_word:
					k += 1
					if guess == letter:
						print(f"The letter {guess} is in position {k} of the secret word")
			else:
				print(f"Oh no! the letter {guess} is not part of the secret word!")
				lives -= 1
		else:	
			if guess == secret_word:
				return print(f"\nCongrats, you won! The secret word was {guess}!")
			else:
				print(f"Oh no! {guess} is not the secret word!")
				lives -= 1	
	print("RIP, you made too many mistakes!")
hangman()
