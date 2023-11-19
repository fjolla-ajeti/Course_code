#Task 1

#Create your own implementation of a built-in function enumerate, named with_index(), which takes two parameters: iterable and start,default is 0.
def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start + i, iterable[i]

# Example usage:

my_list = ['apple', 'banana', 'orange']

for index, value in with_index(my_list, 1):
    print(f'Index {index}: {value}')
