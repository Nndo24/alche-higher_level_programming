#!/usr/bin/python3
secret_number = "7"
guess = ""
while guess != secret_number:
    guess = input("Guess the single-digit secret number (1-9): ")
    if guess != secret_number:
        print("Incorrect! The door remains locked. Try again.")
print("Correct! The magic door swings open.")
