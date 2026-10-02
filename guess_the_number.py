import random

secret_number = random.randint(1, 10)
guess_count = 1

print("I'm thinking of a number between 1 and 10. You have 3 attempts!")

while guess_count <= 3:
    guess = int(input(f"Attempt {guess_count} - Guess the number: "))
    guess_count += 1

    if guess == secret_number:
        print("You won!")
        break
else:
    print(f"Sorry! You ran out of guesses. The secret number was {secret_number}.")
