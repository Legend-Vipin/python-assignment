# 7. Find the sum of all integer numbers in a list or tuple
def sum_of_integers(numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers_list = [10, 20, 30, 40, 50]
    numbers_tuple = (10, 20, 30, 40, 50)
    print(f"Sum of integers in list: {sum_of_integers(numbers_list)}")
    print(f"Sum of integers in tuple: {sum_of_integers(numbers_tuple)}")
