#!/usr/bin/python3
# Quest 26: The Simple Calculator
# Concept: Function dispatch via conditional checks.

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return a / b if b != 0 else "Error: Division by zero!"

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ").strip()
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", subtract(num1, num2))
elif op == "*":
    print("Result:", multiply(num1, num2))
elif op == "/":
    print("Result:", divide(num1, num2))
else:
    print("Unknown arcane operator!")
