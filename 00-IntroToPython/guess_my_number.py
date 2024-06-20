import random

print("Guess My Number")

# This is a Comment
# Select a secret random number (1 to 100)
# Start a counter at 0 to track the number of attempts
# Start loop that runs until number is found
#    Increment the counter by 1
#    Ask user to make a guess, get that guess
#   If guess is > secret number, then say "too high, guess higher"
#   If guess is < secret number, then say "too low, guess lower"

# Tell the user how many guesses they took to get the number
secret_number = random.randint(1, 100)
# print(secret_number)
attempts = 0

while True:

    guess = int(input("Guess the secret number (between 1 and 100): "))
    attempts += 1
    if guess > secret_number:
        print("Too high, guess lower")

    if guess < secret_number:
        print("Too low, guess higher")

    if guess == secret_number:
        print("Correct!")
        print(f"Number of guesses--> {attempts}")
        break
