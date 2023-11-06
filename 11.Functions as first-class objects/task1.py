
#Task 1

#Write a Python program to detect the number of local variables declared in a function.

def count_local_variables():
 
    a = 10
    b = "Hello"
    c = [1, 2, 3]

   
    local_vars = locals()

    
    count = len(local_vars)

    return count


num_locals = count_local_variables()
print("Number of local variables:", num_locals)
