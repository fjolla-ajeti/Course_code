#Task 2

#Writing tests for context manager

#Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. And also, write tests when your class raises errors or you have errors in the runtime context suite.

import unittest
import os

class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.txt"
        with open(self.file_path, "w") as test_file:
            test_file.write("Test content")

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_context_manager_successful_open(self):
        with FileContextManager(self.file_path, "r") as file:
            content = file.read()
            self.assertEqual(content, "Test content")
       

    def test_file_context_manager_multiple_open_close(self):
        with FileContextManager(self.file_path, "r") as file1:
            with FileContextManager(self.file_path, "r") as file2:
                content1 = file1.read()
                content2 = file2.read()
                self.assertEqual(content1, "Test content")
                self.assertEqual(content2, "Test content")
       

    def test_file_context_manager_exception_handling(self):
        with self.assertRaises(Exception):
            with FileContextManager("nonexistent_file.txt", "r") as file:
                content = file.read()
               

    def test_file_context_manager_exception_logging(self):
        with self.assertLogs(level="ERROR") as log:
            with FileContextManager(self.file_path, "w") as file:
                
                file.write("New content")
        self.assertTrue("An exception of type" in log.output[0])

if __name__ == "__main__":
    unittest.main()
