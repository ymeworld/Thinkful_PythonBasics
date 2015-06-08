
#!/usr/bin/python3

import random

number = random.randint(0, 100)
tries = 1

guess = int(input("Enter your guess: "))

while guess != number and tries < 5:
    if guess > number:
        print("Too High")
    else:
        print("Too Low")

    tries += 1
    guess = int(input("Enter your guess: "))

if guess != number:
    print("You lost, the number is: ", number)
else:
    print("You got it right!. The number was: ", number)
