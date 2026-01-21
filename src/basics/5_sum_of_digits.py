# 5. Find the sum of digits in a number
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"The sum of digits in {n} is: {sum_of_digits(n)}")