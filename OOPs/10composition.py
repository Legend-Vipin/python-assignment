# 10. Composition (Part-Of, stronger 'whole-part')
# Concept: Whole owns parts; parts cannot exist independently
class Room:
    def __init__(self, name, size_sqft):
        self.name = name
        self.size_sqft = size_sqft
        print(f"  Constructing Room: {self.name} ({self.size_sqft} sqft)")

    def __del__(self):
        print(f"  Destroying Room: {self.name}")

    def describe(self):
        return f"{self.name} ({self.size_sqft} sqft)"

class House:
    def __init__(self, address):
        self.address = address
        print(f"Constructing House at {self.address}")
        self.living_room = Room("Living Room", 300)
        self.kitchen = Room("Kitchen", 150)
        self.bedrooms = [Room("Bedroom 1", 120), Room("Bedroom 2", 100)]

    def __del__(self):
        print(f"Destroying House at {self.address}")

    def describe_house(self):
        print(f"\nHouse Description ({self.address}):")
        print(f"- {self.living_room.describe()}")
        print(f"- {self.kitchen.describe()}")
        for room in self.bedrooms:
            print(f"- {room.describe()}")

my_home = House("42 Evergreen Terrace")
my_home.describe_house()
del my_home
