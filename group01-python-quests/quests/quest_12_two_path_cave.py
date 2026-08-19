#!/usr/bin/python3
secret_password = "Mellon"
user_entry = input("Speak the secret word to enter: ")
if user_entry == secret_password:
    print("Access Granted! The iron gate grinds open.")
else:
    print("Access Denied! The guards raise their spears.")
