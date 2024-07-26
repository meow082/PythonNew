import random

secret = random.randint(1, 100) # generate a random number between 1 and 100
min_value = 1
max_value = 100

while True:
    guess = input(f"Please guess the number between {min_value} and {max_value}: ")
    if int(guess) < min_value or int(guess) > max_value:
        print("Please guess the number within the range.")
        continue

    if int(guess) == secret:
        print(f"Congratulations! The secret number is {secret}.")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)