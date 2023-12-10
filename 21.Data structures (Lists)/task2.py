
#Task 2

#Implement a stack using a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek()) 
print(stack.pop())   
print(stack.pop())   
print(stack.peek())  
