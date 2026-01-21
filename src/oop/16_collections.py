# -*- coding: utf-8 -*-
"""
Illustrations for Working with Collections of Objects

This file covers:
2. Working with Collections (list, tuple, set, dict) of Objects
"""

import importlib.util
import sys
from pathlib import Path

# Load the class_anatomy module
module_path = Path(__file__).parent / "15_class_anatomy.py"
spec = importlib.util.spec_from_file_location("class_anatomy", module_path)
class_anatomy = importlib.util.module_from_spec(spec)
sys.modules["class_anatomy"] = class_anatomy
spec.loader.exec_module(class_anatomy)

# Import needed objects
Car = class_anatomy.Car
car1 = class_anatomy.car1
car2 = class_anatomy.car2
car3 = class_anatomy.car3
car4 = class_anatomy.car4

#==============================================================================
# Part 2: Collections of Objects (List, Tuple, Set, Dict)
#==============================================================================
print("\n\n--- Part 2: Collections of Objects ---")

# We have car1, car2, car3, car4 already created. Let's add one more.
car5 = Car("Tesla", "Model 3", 2021, 22000)

# --- List of Objects ---
# Mutable, ordered sequence. Allows duplicates.
print("\n--- List ---")
car_list = [car1, car2, car3, car4, car5]
print(f"Original List (uses __repr__): {car_list}")

print("\nLooping through the list:")
for car in car_list:
    print(f"  - {car.get_description()}") # Access methods/attributes via the loop variable

print(f"\nAccessing by index (e.g., first car): {car_list[0]}")
print(f"Accessing attribute of third car: {car_list[2].make}")

# --- Tuple of Objects ---
# Immutable, ordered sequence. Allows duplicates.
print("\n--- Tuple ---")
car_tuple = (car1, car2, car3, car4, car5)
print(f"Original Tuple: {car_tuple}")

print("\nLooping through the tuple:")
for i, car in enumerate(car_tuple): # Using enumerate to get index too
    print(f"  - Index {i}: {car.year} {car.model}")

print(f"\nAccessing by index (e.g., last car): {car_tuple[-1]}")
# car_tuple[0] = car5 # This would cause a TypeError: 'tuple' object does not support item assignment

# --- Set of Objects ---
# Unordered collection of unique items. Requires objects to be hashable (__hash__ and __eq__).
print("\n--- Set ---")
# car4 is equal to car1 based on our __eq__ definition, so it will be excluded.
car_set = {car1, car2, car3, car4, car5}
print(f"Original Set (order not guaranteed, duplicates based on __eq__ removed): {car_set}")

print("\nLooping through the set:")
for car in car_set:
    print(f"  - Make: {car.make}, Model: {car.model}, Year: {car.year}") # Access attributes

# Checking for membership (efficient in sets)
print(f"\nIs car3 in the set? {car3 in car_set}")
temp_car = Car("Honda", "Civic", 2018) # Create a car equal to car2
print(f"Is a new 2018 Civic in the set? {temp_car in car_set}") # True because of __eq__ and __hash__

# Cannot access by index: car_set[0] would raise a TypeError

# --- Dictionary of Objects ---
# Key-value store. Keys must be unique and hashable. Values can be anything (our objects).
print("\n--- Dictionary ---")
# Let's use a unique ID or tuple (make, model, year) as keys
car_dict = {
    f"{c.make}_{c.model}_{c.year}": c for c in car_set # Using a dictionary comprehension
}
# Or manually:
# car_dict = {
#     "Toyota_Camry_2020": car1, # Note car4 would overwrite car1 if key is the same
#     "Honda_Civic_2018": car2,
#     "Ford_Mustang_1967": car3,
#     "Tesla_Model_3_2021": car5
# }

print(f"Dictionary Keys: {list(car_dict.keys())}")
print(f"Dictionary Values (Objects): {list(car_dict.values())}")

print("\nLooping through dictionary items (key-value pairs):")
for key, car in car_dict.items():
    print(f"  - Key '{key}': {car.get_description()}")

print("\nLooping through dictionary values (the objects):")
for car in car_dict.values():
    print(f"  - Car Mileage: {car.mileage}")

# Accessing by key (efficient)
lookup_key = "Ford_Mustang_1967"
print(f"\nAccessing car with key '{lookup_key}': {car_dict[lookup_key]}")

# Safe access using .get()
non_existent_key = "BMW_X5_2022"
print(f"Accessing key '{non_existent_key}' safely: {car_dict.get(non_existent_key, 'Car not found')}")
