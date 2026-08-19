#!/usr/bin/python3
def personalized_greeting(name, quest):
    print(f"Hail, {name}! May your quest to '{quest}' bring glory to the kingdom.")
user_name = input("Enter your hero name: ")
user_quest = input("Enter your quest objective: ")
personalized_greeting(user_name, user_quest)
