# Examples of Higher Order Functions, First Class Functions, and Lambda Expressions

def apply_function(f, value):
    return f(value)

def square(x):
    return x * x

def cube(x):
    return x * x * x

# Using a higher order function
print("Square of 5:", apply_function(square, 5))
print("Cube of 3:", apply_function(cube, 3))

# Using lambda expressions
print("Double of 4:", apply_function(lambda x: x * 2, 4))
print("Increment 7 by 1:", apply_function(lambda x: x + 1, 7))

# Functions as first class objects
def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

def greet(func):
    greeting = func("Hello")
    print(greeting)

greet(shout)
greet(whisper)
