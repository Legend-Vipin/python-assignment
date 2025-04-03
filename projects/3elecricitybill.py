class ElectricityBillCalculator:
    def __init__(self, unit, price, days):
        self.unit = unit
        self.price = price
        self.days = days
    
    def calculate_bill(self):
        return (self.unit / 30 * self.days) * self.price

def main():
    try:
        unit = int(input("Enter unit: "))
        price = int(input("Enter price: "))
        days = int(input("Enter days: "))
        
        calculator = ElectricityBillCalculator(unit, price, days)
        bill = calculator.calculate_bill()
        print(f"Electricity bill is: {bill}")
    except ValueError:
        print("Please enter valid numeric values")

if __name__ == "__main__":
    main()