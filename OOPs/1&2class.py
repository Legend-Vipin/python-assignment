# 1. Class
# Concept: Blueprint/template (e.g., Cookie Cutter, Recipe, Blueprint)
class CarBlueprint:
    """
    This class acts as a blueprint (like an architect's plan)
    for creating car objects. It defines attributes and methods.
    """
    vehicle_type = "Automobile"

    def __init__(self, color, model):
        print(f"Building a new car based on the '{model}' blueprint...")
        self.color = color
        self.model = model
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            print(f"Starting the {self.color} {self.model}'s engine. Vroom!")
            self.engine_started = True
        else:
            print("Engine is already running.")

    def display_info(self):
        print(f"This car is a {self.color} {self.model} ({self.vehicle_type}). Engine running: {self.engine_started}")

print("Defined the CarBlueprint class.")
CarBlueprint("Red", "Toyota Camry")
# 2. Object
# Concept: Specific instance created from a class (e.g., The actual cookie, my house, the baked cake)
print("--- 2. Object ---")

# Creating specific instances (objects) using the CarBlueprint class (the 'cookie cutter')
my_sedan = CarBlueprint("Red", "Sedan")      # This is one object (one specific 'cookie')
your_suv = CarBlueprint("Blue", "SUV")      # This is another object (another specific 'cookie')
neighbor_truck = CarBlueprint("Black", "Truck") # A third object

print("\nCreated specific car objects from the blueprint:")
# Each object has its own state (attribute values) but shares the class structure
my_sedan.display_info()
your_suv.display_info()
neighbor_truck.display_info()

# Interact with a specific object's methods
my_sedan.start_engine()
my_sedan.display_info() # State of my_sedan has changed
your_suv.display_info() # State of your_suv remains unchanged

print("\nObjects are distinct instances of a class.\n")