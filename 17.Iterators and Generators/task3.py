#Task 3

#Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax.

class CustomIterable:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        return self.data[index]



custom_list = CustomIterable([1, 2, 3, 4, 5])


for item in custom_list:
    print(item)


print(custom_list[2]) 
print(custom_list[4]) 
