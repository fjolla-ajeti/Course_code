#Task 4

#The math quiz program

#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

import random


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)


operator = random.choice(['+', '-'])

if operator == '+':
    correct_answer = num1 + num2
else:
    correct_answer = num1 - num2


user_answer = int(input(f"What is {num1} {operator} {num2}? "))


if user_answer == correct_answer:
    print("Correct! Well done.")
else:
    print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")
