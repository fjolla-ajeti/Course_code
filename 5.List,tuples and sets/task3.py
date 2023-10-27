#Task 3

#Extracting numbers.

#Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

#Constraint: use only while loop for iteration.



all_numbers = list(range(1, 101))


result_list = []


index = 0
while index < len(all_numbers):
    number = all_numbers[index]

    if number % 7 == 0 and number % 5 != 0:
        result_list.append(number)

    index += 1

print(result_list)
