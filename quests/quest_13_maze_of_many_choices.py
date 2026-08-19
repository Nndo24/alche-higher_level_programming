#!/usr/bin/python3
score = float(input("Enter your magic exam score (0-100): "))
if score >= 90:
    print("Rank: A - Archmage Status!")
elif score >= 80:
    print("Rank: B - Skilled Practitioner.")
elif score >= 70:
    print("Rank: C - Apprentice.")
else:
    print("Rank: Needs Improvement - Back to the library!")
