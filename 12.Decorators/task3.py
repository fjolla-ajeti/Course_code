
#Task 3

#Write a decorator arg_rules() that validates arguments passed to the function.

#A decorator should take 3 arguments:

#max_length: 15

#type_: str

#contains: [] - list of symbols that an argument should contain

#If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.



def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_) or len(arg) > max_length or not all(symbol in arg for symbol in contains):
                print("Invalid argument.")
                return False
            return func(arg)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
