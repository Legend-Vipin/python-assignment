# Introduction to Units (Modules), Importing Units, and Abstract Data Types (ADT) in Python
# Example of importing a unit (module)
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

# Abstract Data Type example: Stack interface and implementation

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

if __name__ == "__main__":
    print("Area of circle with radius 5:", calculate_circle_area(5))

    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack size:", stack.size())
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack size after pop:", stack.size())
