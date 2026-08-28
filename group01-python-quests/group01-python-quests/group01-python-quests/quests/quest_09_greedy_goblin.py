#!/usr/bin/python3
# Quest 9: The Greedy Goblin
# Concept: Integer division (//) and Modulo (%).

total_gold = 27
friends_count = 4

share_per_friend = total_gold // friends_count
goblin_remainder = total_gold % friends_count

print(f"Each friend receives {share_per_friend} gold pieces.")
print(f"The greedy goblin keeps the remaining {goblin_remainder} gold piece(s) for himself!")
