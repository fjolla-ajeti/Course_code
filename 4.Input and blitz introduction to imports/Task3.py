# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string

import random

input_string = input("Enter a string: ")

if input_string:
    for i in range(5):
        random_string = ''.join(random.choice(input_string) for i in range(len(input_string)))
        print(random_string)
else:
    print("Please enter a valid string.")

