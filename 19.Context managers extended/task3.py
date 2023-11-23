#Task 3 (Optional)

#Pytest fixtures with context manager

#Create a simple function, which performs any logic of your choice with text data, which it obtains from a file object, passed to this function ( def test(file_obj) ). 

#Create a test case for this function using pytest library (Full pytest documentation).  

#Create pytest fixture, which uses your implementation of the context manager to return a file object, which could be used inside your function.

import pytest


class FileProcessor:
    def process_file(self, file_obj):
        
        content = file_obj.read()
        lines = content.split('\n')
        return len(lines)


@pytest.fixture
def file_obj_fixture():
    file_path = "test_fixture_file.txt"
    with open(file_path, "w") as test_file:
        test_file.write("Line 1\nLine 2\nLine 3")
    
    with FileContextManager(file_path, "r") as file_obj:
        yield file_obj

    if os.path.exists(file_path):
        os.remove(file_path)


def test_file_processor(file_obj_fixture):
    processor = FileProcessor()
    result = processor.process_file(file_obj_fixture)
    assert result == 3  