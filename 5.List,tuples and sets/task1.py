#The greatest number

#Write a Python program to get the largest number from a list of random numbers with the length of 10

#Constraints: use only while loop and random module to generate numbers

import random

random_numbers = []


count = 0
while count < 10:
    random_numbers.append(random.randint(1, 100)) 
    count += 1


largest_number = max(random_numbers)

print("Generated random numbers:", random_numbers)
print("The largest number is:", largest_number)
