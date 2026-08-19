#!/usr/bin/python3
# Quest 12: The Two-Path Cave
# Concept: if-else control structures.

secret_password = "Mellon"
user_entry = input("Speak the secret word to enter: ")
if user_entry == secret_password:
    print("Access Granted! The iron gate grinds open.")
else:
    print("Access Denied! The guards raise their spears.")
