# exceptions_assertions.py
# Examples of Exception Handling and Assertions in Python

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        return None
    else:
        print(f"Result of {a} / {b} is {result}")
        return result
    finally:
        print("Execution of divide function complete.")

def check_positive(number):
    assert number > 0, "Number must be positive"
    print(f"{number} is positive.")

if __name__ == "__main__":
    # Exception handling example
    divide(10, 2)
    divide(5, 0)

    # Assertion example
    try:
        check_positive(5)
        check_positive(-3)
    except AssertionError as e:
        print(f"AssertionError: {e}")
