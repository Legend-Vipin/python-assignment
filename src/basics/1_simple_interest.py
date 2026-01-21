# 1. Calculate the simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    print(f"The Simple Interest is: {simple_interest}")

if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time in years: "))
    
    calculate_simple_interest(principal, rate, time)
