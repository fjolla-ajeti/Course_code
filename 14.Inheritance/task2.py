# Task 2
# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    def square_nums(self, list_integers):
        return [num**2 for num in list_integers]

    def remove_positives(self, list_integers1):
        return [num for num in list_integers1 if num <= 0]

    def filter_leaps(self, dates):
        return [year for year in dates if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
print(m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90])
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020])