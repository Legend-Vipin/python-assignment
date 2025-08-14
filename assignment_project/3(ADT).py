# Example representing the interface of a Stack ADT in Python

# A Stack is an ADT that follows the Last-In, First-Out (LIFO) principle.
# Operations: push (add item), pop (remove top item), peek (view top item), is_empty.

class StackADT:
    """
    Abstract Data Type representing a Stack.

    This class defines the interface for a Stack, specifying the operations
    that a concrete Stack implementation must support. It does NOT provide
    the actual implementation details (e.g., using a list or linked list).
    """

    def __init__(self):
        """Initializes an empty Stack."""
        # In a real ADT interface, you might not have initialization details,
        # but for a conceptual Python representation, it sets the stage.
        # The internal data structure is NOT exposed here.
        pass # This is just the interface definition

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The item to add.
        """
        # This method signature defines the 'push' operation.
        # The specific code to add the item (e.g., list.append()) is
        # part of the concrete implementation, not the ADT interface.
        raise NotImplementedError("Subclass must implement abstract method")

    def pop(self):
        """
        Removes and returns the item from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        # This method signature defines the 'pop' operation and its behavior
        # (returns the top item, raises error if empty).
        raise NotImplementedError("Subclass must implement abstract method")

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        # Defines the 'peek' operation and its behavior.
        raise NotImplementedError("Subclass must implement abstract method")

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        # Defines the 'is_empty' operation.
        raise NotImplementedError("Subclass must implement abstract method")

    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items.
        """
        # Defines the 'size' operation.
        raise NotImplementedError("Subclass must implement abstract method")


# A concrete implementation of the Stack ADT using Python's list
class ListStack(StackADT):
    """
    A concrete implementation of the Stack ADT using a Python list.
    """
    def __init__(self):
        """Initializes an empty list to store stack items."""
        self._items = [] # The internal data structure (a list)

    def push(self, item):
        """Adds an item to the top of the stack (end of the list)."""
        self._items.append(item)

    def pop(self):
        """Removes and returns the item from the top (end) of the list."""
        return self._items.pop() # list.pop() handles the empty case with IndexError

    def peek(self):
        """Returns the item from the top (end) of the list without removing."""
        if not self.is_empty():
            return self._items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        """Checks if the list is empty."""
        return len(self._items) == 0

    def size(self):
        """Returns the number of items in the list."""
        return len(self._items)

# Example usage of the concrete implementation
my_stack = ListStack()
print("Is stack empty?", my_stack.is_empty()) # Output: Is stack empty? True
my_stack.push(10)
my_stack.push(20)
print("Stack size:", my_stack.size())       # Output: Stack size: 2
print("Top element (peek):", my_stack.peek()) # Output: Top element (peek): 20
print("Popped element:", my_stack.pop())    # Output: Popped element: 20
print("Is stack empty?", my_stack.is_empty()) # Output: Is stack empty? False
print("Popped element:", my_stack.pop())    # Output: Popped element: 10
print("Is stack empty?", my_stack.is_empty()) # Output: Is stack empty? True

try:
    my_stack.pop() # This will raise an IndexError
except IndexError as e:
    print(f"Caught expected error: {e}") # Output: Caught expected error: pop from empty list