#!/usr/bin/python3
# Quest 24: The Master Spell
# Concept: Composing functions together.

def ask_for_age():
    return int(input("Please state your age: "))

def can_they_vote(age):
    if age >= 18:
        print("You are eligible to vote in the high council.")
    else:
        print("You are too young to vote in the high council.")

# Executing composite logic
user_age = ask_for_age()
can_they_vote(user_age)
