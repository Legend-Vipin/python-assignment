# 3. Print Fibonacci series till n numbers using recursion
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"The Fibonacci series till {n} numbers is:")
    for i in range(n):
        print(fibonacci(i), end=" ")