# -*- coding: utf-8 -*-
"""
Illustrations for Python Class Anatomy

This file covers:
1. Anatomy of a Python Class (Attributes, Methods, self, Class Attributes, etc.)
"""

# Make sure outputs are printed in Colab
import sys
import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # Usually not needed in modern Colab

print("--- Python Class Illustrations ---")

#==============================================================================
# Part 1: Anatomy of a Python Class
#==============================================================================
print("\n\n--- Part 1: Anatomy of a Python Class ---")

# --- Global Variable ---
# Defined outside any function or class. Accessible anywhere in the module.
global_app_version: str = "1.0"
print(f"\n[Global Scope] Initial App Version: {global_app_version}")

class Car:
    """
    Represents a car with make, model, year, and mileage.
    Illustrates class anatomy: attributes, methods, self, etc.
    """

    # --- Class Attribute ---
    # Shared by ALL instances of the class. Accessed using ClassName.attribute
    # Doesn't use 'self'. It belongs to the class itself.
    number_of_wheels = 4
    vehicle_type = "Automobile"

    def __init__(self, make, model, year, mileage=0):
        """
        The Initializer (often called Constructor). Called when you create a new object.
        'self': Represents the specific instance (object) being created or worked on.
                It's the first parameter in instance methods by convention.
                It allows you to access attributes and methods specific to this object.

        Instance Attributes (Variables): Data unique to each object (each car).
                                         Defined using 'self.attribute_name'.
        """
        print(f"\n[__init__] Initializing a new Car object (using 'self' to set attributes)")
        self.make = make          # Instance attribute
        self.model = model        # Instance attribute
        self.year = year          # Instance attribute
        self.mileage = mileage    # Instance attribute

        # --- Local Variable ---
        # Defined inside a method/function. Only exists within that method's scope.
        init_message = f"Created a {self.year} {self.make} {self.model}."
        print(f"[__init__ Scope] Local variable message: {init_message}")

    # --- Instance Method (Operation) ---
    # Operates on a specific instance of the class. Requires 'self'.
    def get_description(self):
        """Returns a string describing the car."""
        # Accesses instance attributes using 'self'.
        # 'description' here is a local variable within the method.
        description = f"{self.year} {self.make} {self.model} with {self.mileage} miles."
        return description

    # --- Another Instance Method ---
    def drive(self, distance):
        """Simulates driving the car, increasing its mileage."""
        # Modifies an instance attribute.
        if distance > 0:
            self.mileage += distance
            # Accessing a global variable (read-only is fine)
            print(f"[drive Method] Drove {distance} miles. Total mileage: {self.mileage}. (App Version: {global_app_version})")
        else:
            print("[drive Method] Distance must be positive.")

    # --- Method demonstrating NOT using 'self' (Class Method) ---
    @classmethod
    def get_vehicle_type(cls):
        """
        Class Method: Operates on the class itself, not instances.
        Uses 'cls' (by convention) instead of 'self' to refer to the class.
        Can access class attributes.
        """
        # 'cls' refers to the 'Car' class here
        return f"This is a type of: {cls.vehicle_type}. All instances have {cls.number_of_wheels} wheels."

    # --- Method demonstrating NOT using 'self' or 'cls' (Static Method) ---
    @staticmethod
    def get_generic_advice():
        """
        Static Method: Doesn't depend on instance state ('self') or class state ('cls').
        Often utility functions related to the class concept. Behaves like a regular function
        but is grouped within the class's namespace.
        """
        return "Always drive safely and follow traffic rules."

    # --- Property (Optional but good practice) ---
    # Provides controlled access to an attribute. Looks like an attribute access
    # but can run code (e.g., for validation).
    @property
    def is_vintage(self):
        """A property that determines if the car is vintage (e.g., > 30 years old)."""
        import datetime
        current_year = datetime.datetime.now().year
        return (current_year - self.year) > 30

    # --- Special Methods (Dunder Methods) ---
    def __str__(self):
        """String representation for user-friendly output (e.g., print(my_car))."""
        return f"Car({self.year} {self.make} {self.model})"

    def __repr__(self):
        """Official string representation, useful for debugging (e.g., when printing lists of objects)."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, mileage={self.mileage})"

    # Needed for sorting if comparing objects directly, or for sets based on content
    def __eq__(self, other):
        """Defines equality comparison (==) between Car objects."""
        if not isinstance(other, Car):
            return NotImplemented # Important: lets Python handle comparison with other types
        # Let's say two cars are equal if they have the same make, model, and year
        return (self.make == other.make and
                self.model == other.model and
                self.year == other.year)

    def __hash__(self):
        """
        Required if you define __eq__ and want objects to be usable in sets or dict keys.
        Should return an integer. Objects that compare equal should have the same hash.
        """
        # Hash based on the attributes used in __eq__
        return hash((self.make, self.model, self.year))

    def __lt__(self, other):
        """Defines less than comparison (<), used for default sorting."""
        if not isinstance(other, Car):
            return NotImplemented
        # Default sort by year, then make, then model
        return (self.year, self.make, self.model) < (other.year, other.make, other.model)


# --- Using the Class ---
print("\n--- Demonstrating Class Usage ---")

# Create instances (objects) of the Car class
car1 = Car("Toyota", "Camry", 2020, 15000)
car2 = Car("Honda", "Civic", 2018) # Mileage defaults to 0
car3 = Car("Ford", "Mustang", 1967, 85000)
car4 = Car("Toyota", "Camry", 2020, 500) # Same make/model/year as car1

print(f"\nInstance 1: {car1}") # Uses __str__
print(f"Instance 2 Description: {car2.get_description()}") # Call instance method

# Accessing instance attributes
print(f"Car 3 Mileage: {car3.mileage}")
car3.drive(150) # Call instance method modifying state
print(f"Car 3 Mileage after driving: {car3.mileage}")

# Accessing Class Attributes (can use Class name or instance name)
print(f"\nNumber of wheels (via Class): {Car.number_of_wheels}")
print(f"Number of wheels (via instance car1): {car1.number_of_wheels}")

# Calling Class Method and Static Method (use Class name)
print(f"Vehicle Type Info (Class Method): {Car.get_vehicle_type()}")
print(f"Generic Advice (Static Method): {Car.get_generic_advice()}")

# Accessing the property
print(f"Is Car 1 vintage? {car1.is_vintage}")
print(f"Is Car 3 vintage? {car3.is_vintage}")

# Demonstrating __eq__
print(f"\nIs car1 == car2? {car1 == car2}") # False
print(f"Is car1 == car4? {car1 == car4}") # True (based on __eq__ definition)

# --- Global Variable Modification ---
def update_version():
    global global_app_version # Keyword needed to MODIFY a global variable inside a function
    global_app_version = "1.1"
    print(f"\n[Function Scope] Updated global App Version: {global_app_version}")

update_version()
print(f"[Global Scope] App Version after update: {global_app_version}")
# Instance methods can now access the updated global variable
car1.drive(50)
