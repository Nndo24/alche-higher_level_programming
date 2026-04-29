#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list where each element is True if divisible by 2, else False
    return [x % 2 == 0 for x in my_list]
