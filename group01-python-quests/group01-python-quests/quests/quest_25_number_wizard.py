#!/usr/bin/python3
# Quest 25: The Number Wizard
# Concept: Game loop with comparative hints.

import random

secret = random.randint(1, 50)
guessed = False

print("The Wizard has chosen a number between 1 and 50.")
while not guessed:
    guess = int(input("Enter your guess: "))
    if guess < secret:
        print("Too low! The magic rises higher.")
    elif guess > secret:
        print("Too high! Lower your expectations.")
    else:
        print("Spot on! You have defeated the Number Wizard!")
        guessed = True
