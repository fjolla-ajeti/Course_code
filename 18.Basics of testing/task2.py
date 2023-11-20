#Task 2

#Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write tests using unittest library


import unittest

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get_contact(self, name):
        return self.contacts.get(name)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def contact_exists(self, name):
        return name in self.contacts

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.phonebook.add_contact("Alice", "12345")
        self.phonebook.add_contact("Bob", "67890")

    def test_add_contact(self):
        self.phonebook.add_contact("Charlie", "54321")
        self.assertTrue(self.phonebook.contact_exists("Charlie"))

    def test_get_contact(self):
        self.assertEqual(self.phonebook.get_contact("Alice"), "12345")
        self.assertEqual(self.phonebook.get_contact("Bob"), "67890")

    def test_delete_contact(self):
        self.phonebook.delete_contact("Alice")
        self.assertFalse(self.phonebook.contact_exists("Alice"))

    def test_contact_exists(self):
        self.assertTrue(self.phonebook.contact_exists("Alice"))
        self.assertFalse(self.phonebook.contact_exists("Eve"))

if __name__ == '__main__':
    unittest.main()
