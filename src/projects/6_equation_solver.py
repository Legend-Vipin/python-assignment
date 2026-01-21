class Equation:
    def __init__(self, x):
        self.x = x
    
    def solve(self):
        return self.x**3 + 4

def main():
    try:
        x = int(input("Enter x: "))
        equation = Equation(x)
        result = equation.solve()
        print("Answer is:", result)
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
