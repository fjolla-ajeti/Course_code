#Exclusive common numbers.

#Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

#Constraints: use only while loop and random module to generate numbers

import random

list1 = []
list2 = []

count = 0
while count < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    count += 1

print("List 1:", list1)
print("List 2:", list2)

common_list = []

index = 0
while index < 10:
    if list1[index] in list2 and list1[index] not in common_list:
        common_list.append(list1[index])
    index += 1

print("Common List:", common_list)
