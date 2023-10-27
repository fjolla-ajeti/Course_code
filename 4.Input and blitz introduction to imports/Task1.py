#Task 1

#The Guessing Game.

#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
#The result should be sent back to the user via a print statement.

from random import Random 

random_instace=Random()
random_instace=random_instace.randint(0,10)

#user input
user_number=input("Put a random number between 0 and 10 >>")

#check if user input is number
if user_number.isdigit():
    if int(user_number)==random_instace:
        print("You have guess right. WIN WIN")
    else: 
        print("You have guess wrong. LOSS WIN")
else:
    print("You did not put a number")