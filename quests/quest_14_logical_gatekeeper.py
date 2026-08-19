#!/usr/bin/python3
age = int(input("What is your age? "))
gold = int(input("How many gold coins do you possess? "))
if age >= 18 and gold >= 20:
    print("Welcome to the Secret Society Guild hall!")
else:
    print("Begone! You do not meet the age or wealth requirements.")
