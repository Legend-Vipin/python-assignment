class ForceCalculator:
    def __init__(self, mass, acceleration):
        self.mass = mass
        self.acceleration = acceleration
    
    def calculate_force(self):
        return self.mass * self.acceleration

def main():
    try:
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        
        calculator = ForceCalculator(mass, acceleration)
        force = calculator.calculate_force()
        print(f"Force is: {force} Newton")
    except ValueError:
        print("Please enter valid numeric values")

if __name__ == "__main__":
    main()