# 3. Inheritance (IS-A Relationship)
# Concept: Deriving properties/methods from a parent class (e.g., Sports Car IS A Car, Robin IS A Bird)
class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def move(self):
        print(f"{self.name} is moving.")

class ElectricCar(Vehicle):
    def __init__(self, name, battery_capacity):
        super().__init__(name, wheels=4)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.name} is charging its {self.battery_capacity}kWh battery.")

    def move(self):
        print(f"{self.name} glides silently.")

my_tesla = ElectricCar("Tesla Model S", 100)

print(f"Vehicle Name: {my_tesla.name}")
print(f"Number of Wheels: {my_tesla.wheels}")
my_tesla.charge()
my_tesla.move()
