class LabAreaCalculator:
    def __init__(self):
        self.areas = []
    
    def add_area(self, length, width):
        area = length * width
        self.areas.append(area)
        return area
    
    def get_total_area(self):
        return sum(self.areas)

def main():
    calculator = LabAreaCalculator()
    
    # Calculate areas for doors
    door1_area = calculator.add_area(5, 2)
    door2_area = calculator.add_area(34, 4)
    
    total_area = calculator.get_total_area()
    print(f"Total area: {total_area}")

if __name__ == "__main__":
    main()