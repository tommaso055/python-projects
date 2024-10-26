import random 
def number_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_number:
                print("\ntry higher...")
            elif guess > random_number:
                print("\ntry lower...")
        except:
            print("\nthe secret number is an integer...")
    print(f"Well done! The secret number was {guess}!")
number_guess(100)