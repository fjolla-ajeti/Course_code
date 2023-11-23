#Task 1

#File Context Manager class

#Create your own class, which can behave like a built-in function open(). Also, you need to extend its functionality with counter and logging. Pay special attention to the implementation of __exit__ method, which has to cover all the requirements to context managers mentioned here:

#Context Manager Types 

#The with statement 


import logging

class FileContextManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        self.counter += 1
        logging.info(f"File '{self.file_name}' opened. Counter: {self.counter}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        logging.info(f"File '{self.file_name}' closed. Counter: {self.counter}")
        if self.file:
            self.file.close()
        if exc_type is not None:
            logging.error(f"An exception of type {exc_type} occurred with value {exc_value}")
        return False  

file_path = "example.txt"


with FileContextManager(file_path, "w") as file:
    file.write("Hello, this is a test.")


 







