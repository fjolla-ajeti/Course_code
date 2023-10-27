#Task 2

#The birthday greeting program.

#Write a program that takes your name as input, and then your age as input and greets you with the following:

name_input=input("Please give you name:")
age_input=input("Please give age input: ")

if(len(name_input)>0 and len(age_input))>0:
    if age_input.isdigit():
        next_age=int(age_input)+1
        print(f"Hello {name_input}, on your next birthday you'll be {next_age} years")
    else:
        print("Age is not a number")
else:
    print("You didn't answerd as expected")