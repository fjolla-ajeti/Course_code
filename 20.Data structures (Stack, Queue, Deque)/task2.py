#Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

def is_balanced(sequence):
    stack = Stack()
    opening_brackets = "({["  # Opening brackets
    closing_brackets = ")}]"  # Closing brackets

    for char in sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_item = stack.pop()
            if opening_brackets.index(top_item) != closing_brackets.index(char):
                return False

    return stack.is_empty()

input_sequence = input("Enter a sequence of characters: ")

if is_balanced(input_sequence):
    print("The sequence has balanced parentheses, braces, and curly brackets.")
else:
    print("The sequence does not have balanced parentheses, braces, and curly brackets.")
