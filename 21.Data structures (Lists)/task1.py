#Task1 
#Extend UnorderedList

#Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two parameters start and stop, and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        self.add(item)

    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1
        if not found:
            raise ValueError("Item not in list")
        return index

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        current = self.head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = None
        else:
            previous.set_next(None)
        return current.get_data()

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("Insert index out of range")
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            count = 0
            while count < pos:
                previous = current
                current = current.get_next()
                count += 1
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)

    def slice(self, start, stop):
        if start < 0 or stop > self.size() or start >= stop:
            raise ValueError("Invalid slice indices")
        current = self.head
        count = 0
        sliced_list = UnorderedList()
        while current is not None:
            if start <= count < stop:
                sliced_list.append(current.get_data())
            current = current.get_next()
            count += 1
        return sliced_list


# Example usage:

my_list = UnorderedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)

current_node = my_list.head
result = []
while current_node is not None:
    result.append(current_node.get_data())
    current_node = current_node.get_next()
print("Original list:", result)

# Test append, index, pop, insert methods
my_list.append(6)
current_node = my_list.head
result = []
while current_node is not None:
    result.append(current_node.get_data())
    current_node = current_node.get_next()
print("After append:", result)

print("Index of 3:", my_list.index(3))

print("Popped element:", my_list.pop())
current_node = my_list.head
result = []
while current_node is not None:
    result.append(current_node.get_data())
    current_node = current_node.get_next()
print("List after pop:", result)

my_list.insert(2, 10)
current_node = my_list.head
result = []
while current_node is not None:
    result.append(current_node.get_data())
    current_node = current_node.get_next()
print("List after insertion at position 2:", result)

# Test slice method
sliced = my_list.slice(1, 4)
current_node = sliced.head
result = []
while current_node is not None:
    result.append(current_node.get_data())
    current_node = current_node.get_next()
print("Sliced list:", result)
