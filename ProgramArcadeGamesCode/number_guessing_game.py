import random

secret_number = random.randrange(1, 129)

guess = 0
while guess != secret_number:
    guess = (int)(input("Guess a number 1 to 128: "))
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct!")
