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

    def get_from_stack(self, element):
        found = False
        found_element = None
        temp_stack = Stack()

        while not self.is_empty():
            current = self.pop()
            if current == element and not found:
                found_element = current
                found = True
            else:
                temp_stack.push(current)

     
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return found_element
        else:
            raise ValueError(f"Element '{element}' not found in the stack")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

try:
    element = stack.get_from_stack(3)
    print(f"Found element: {element}")
except ValueError as e:
    print(e)

try:
    element = stack.get_from_stack(5)
    print(f"Found element: {element}")
except ValueError as e:
    print(e)
