secret_word = "cecio"
guess = ""
lives = 5

print("Welcome to the guessing game: try to guess the secret word")

while lives > 0:
    if lives > 1:
        print("\nYou have " + str(lives) + " lives")
    else:
        print("\nYou have " + str(lives) + " life")
    guess = input("Enter your guess: ")
    if guess != secret_word:
        lives -= 1
        print("\nYou're wrong! Try again...")
    else:
        break
if guess == secret_word:
    print("\nyou won!")
else:
    print("\nyou lost!")



