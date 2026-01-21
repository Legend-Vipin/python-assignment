class UtilityExpenseCalculator:
    def __init__(self):
        # Water constants
        self.water_gallons_per_week = 25
        self.water_cost_per_unit = 25
        self.weeks_per_year = 52
        
        # Electricity constants
        self.electricity_units_per_14days = 200
        self.electricity_cost_per_unit = 7.03
        self.periods_per_year = 365 / 14
    
    def calculate_water_expense(self):
        return (self.water_gallons_per_week * 
                self.water_cost_per_unit * 
                self.weeks_per_year)
    
    def calculate_electricity_expense(self):
        yearly_units = self.electricity_units_per_14days * self.periods_per_year
        return yearly_units * self.electricity_cost_per_unit
    
    def calculate_total_expense(self):
        water_expense = self.calculate_water_expense()
        electricity_expense = self.calculate_electricity_expense()
        return water_expense + electricity_expense
    
    def print_expenses(self):
        water_expense = self.calculate_water_expense()
        electricity_expense = self.calculate_electricity_expense()
        total_expense = self.calculate_total_expense()
        
        print(f"Yearly water expense: ${water_expense:,.2f}")
        print(f"Yearly electricity expense: ${electricity_expense:,.2f}")
        print(f"Total yearly expense: ${total_expense:,.2f}")

def main():
    calculator = UtilityExpenseCalculator()
    calculator.print_expenses()

if __name__ == "__main__":
    main()