#!/usr/bin/python3
SECRET_CODE = "42"
attempts_remaining = 3
while attempts_remaining > 0:
    guess = input(f"Enter secret code ({attempts_remaining} attempts left): ").strip()
    if guess == SECRET_CODE:
        print(" Access Granted! Vault unlocked.")
        break
    else:
        attempts_remaining -= 1
        if attempts_remaining > 0:
            print("Incorrect code! Try again.")
        else:
            print(" Access Denied! Lockout sequence initiated.")
