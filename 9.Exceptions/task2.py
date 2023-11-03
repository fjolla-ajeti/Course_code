#Task 2

#Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).    

def calculate():
    try:
        a = float(input("Enter a number a: "))
        b = float(input("Enter a number b: "))
        
        result = (a ** 2) / b
        return result
    except ValueError:
        raise Exception("Both a and b must be valid numbers.")
    except ZeroDivisionError:
        raise Exception("b cannot be zero; division by zero is not allowed.")

try:
    result = calculate()
    print(f"The result of (a^2) / b is: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
