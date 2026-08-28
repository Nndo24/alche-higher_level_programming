#!/usr/bin/python3
birth_year_str = input("In which year were you born into this realm? ")
birth_year = int(birth_year_str)
current_year = 2026
approximate_age = current_year - birth_year
print(f"By my calculations, you are approximately {approximate_age} years old.")
