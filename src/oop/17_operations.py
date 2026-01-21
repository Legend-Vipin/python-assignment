# -*- coding: utf-8 -*-
"""
Illustrations for Operations on Collections of Objects

This file covers:
3. Operations on Collections (Looping, Accessing, Sorting, Merging, Binary Search Intro)
"""

import importlib.util
import sys
from pathlib import Path

# Load the class_anatomy and collections modules
module_path_1 = Path(__file__).parent / "15_class_anatomy.py"
spec1 = importlib.util.spec_from_file_location("class_anatomy", module_path_1)
class_anatomy = importlib.util.module_from_spec(spec1)
sys.modules["class_anatomy"] = class_anatomy
spec1.loader.exec_module(class_anatomy)

module_path_2 = Path(__file__).parent / "16_collections.py"
spec2 = importlib.util.spec_from_file_location("collections_module", module_path_2)
collections_module = importlib.util.module_from_spec(spec2)
sys.modules["collections_module"] = collections_module
spec2.loader.exec_module(collections_module)

# Import needed objects
Car = class_anatomy.Car
car_list = collections_module.car_list

#==============================================================================
# Part 3: Operations on Collections of Objects
#==============================================================================
print("\n\n--- Part 3: Operations on Collections of Objects ---")

# Using the 'car_list' defined earlier: [car1, car2, car3, car4, car5]
# Remember car1 and car4 are considered equal by __eq__ but are distinct objects in the list

# --- Sorting ---
print("\n--- Sorting Lists ---")

# 1. Default Sort (using __lt__ defined in the class: sorts by year, then make, then model)
# sorted() returns a new sorted list, original list is unchanged.
sorted_list_default = sorted(car_list)
print("Sorted list (default - using __lt__):")
for car in sorted_list_default:
    print(f"  - {car}") # Uses __str__

# 2. Sort using a 'key' function (more flexible)
# Sort by mileage (ascending)
sorted_list_mileage = sorted(car_list, key=lambda car: car.mileage)
print("\nSorted list by mileage (ascending):")
for car in sorted_list_mileage:
    print(f"  - {car.model}: {car.mileage} miles")

# Sort by make (descending)
sorted_list_make_desc = sorted(car_list, key=lambda car: car.make, reverse=True)
print("\nSorted list by make (descending):")
for car in sorted_list_make_desc:
    print(f"  - {car.make} {car.model}")

# In-place sort (modifies the original list)
# car_list.sort(key=lambda car: car.year, reverse=True) # Sorts car_list by year descending
# print("\nOriginal list sorted in-place by year descending:")
# print(car_list)

# --- Merging ---
print("\n--- Merging Lists ---")
new_cars = [
    Car("Chevrolet", "Bolt", 2022, 5000),
    Car("Nissan", "Leaf", 2019, 30000)
]

# Method 1: Using + operator (creates a new list)
merged_list = car_list + new_cars
print(f"Merged list size ({len(merged_list)} items) using + operator.")
print("First few items of merged list:", [str(c) for c in merged_list[:3]]) # Print first 3 using __str__

# Method 2: Using extend() (modifies the first list in-place)
# Create a copy to avoid modifying the original car_list further for subsequent examples
list_to_extend = car_list.copy()
list_to_extend.extend(new_cars)
print(f"\nExtended list size ({len(list_to_extend)} items) using extend().")
print("First few items of extended list:", [str(c) for c in list_to_extend[:3]])


# --- Searching ---
print("\n--- Searching ---")

# 1. Linear Search (checking each element)
target_make = "Honda"
target_model = "Civic"
found_car_linear = None
for car in merged_list:
    if car.make == target_make and car.model == target_model:
        found_car_linear = car
        break # Stop once found

if found_car_linear:
    print(f"Linear Search: Found - {found_car_linear.get_description()}")
else:
    print(f"Linear Search: Car {target_make} {target_model} not found.")

# 2. Binary Search (Much faster, BUT requires the list to be sorted on the key you are searching for)
print("\n--- Binary Search (Introduction) ---")
# Let's search for a car by year in a list sorted by year.
list_sorted_by_year = sorted(merged_list, key=lambda car: car.year)

print("List sorted by year (required for binary search by year):")
for car in list_sorted_by_year:
      print(f"  - {car.year} {car.make} {car.model}")

target_year = 2020

# Python's `bisect` module helps implement binary search efficiently.
import bisect

# We need a way to compare just the year for bisect_left/right
years_only = [car.year for car in list_sorted_by_year]

# Find the index where target_year would be inserted to maintain order
insertion_point = bisect.bisect_left(years_only, target_year)

# Check if the element at the insertion point actually matches the target year
found_cars_bs = []
idx = insertion_point
while idx < len(list_sorted_by_year) and list_sorted_by_year[idx].year == target_year:
    found_cars_bs.append(list_sorted_by_year[idx])
    idx += 1

if found_cars_bs:
     print(f"\nBinary Search (using bisect): Found {len(found_cars_bs)} car(s) from year {target_year}:")
     for car in found_cars_bs:
          print(f"  - {car}")
else:
     print(f"\nBinary Search (using bisect): No cars found from year {target_year}.")

print("\nNote: Binary search is very efficient O(log n) compared to linear search O(n),")
print("but requires the overhead of sorting the list first O(n log n) if it's not already sorted.")

print("\n\n--- End of Illustrations ---")
