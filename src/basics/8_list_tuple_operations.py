# 8. Apply important functions available on lists or tuples in Python.
def important_functions():
    # List
    list1 = [1, 2, 3, 4, 5]
    print("List: ", list1)
    print("Length of list: ", len(list1))
    print("Maximum value in list: ", max(list1))
    print("Minimum value in list: ", min(list1))
    print("Sum of all elements in list: ", sum(list1))
    print("Sorted list: ", sorted(list1))
    print("Reversed list: ", list(reversed(list1)))
    
    list1.append(6)
    print("List after appending 6: ", list1)
    
    list1.remove(6)
    print("List after removing 6: ", list1)
    
    list1.insert(2, 6)
    print("List after inserting 6 at index 2: ", list1)
    
    popped = list1.pop(2)
    print(f"List after popping element at index 2 (removed {popped}): ", list1)
    
    list1.extend([7, 8, 9])
    print("List after extending [7, 8, 9]: ", list1)
    
    list2 = list1.copy()
    print("List after copying: ", list2)
    
    list1.clear()
    print("List after clearing: ", list1)

    # Tuple
    tuple1 = (1, 2, 3, 4, 5)
    print("Tuple: ", tuple1)
    print("Length of tuple: ", len(tuple1))
    print("Maximum value in tuple: ", max(tuple1))
    print("Minimum value in tuple: ", min(tuple1))
    print("Sum of all elements in tuple: ", sum(tuple1))
    print("Sorted tuple: ", sorted(tuple1))
    print("Reversed tuple: ", tuple(reversed(tuple1))
    )
    print("Tuple after appending 6: ", tuple1 + (6,))
    print("Tuple after removing 6: ", tuple1)
    print("Tuple after inserting 6 at index 2: ", tuple1[:2] + (6,) + tuple1[2:])
    print("Tuple after popping element at index 2: ", tuple1[:2] + tuple1[3:])
    print("Tuple after extending [7, 8, 9]: ", tuple1 + (7, 8, 9))
    print("Tuple after clearing: ", tuple())
    print("Tuple after copying: ", tuple1)

if __name__ == "__main__":
    important_functions()