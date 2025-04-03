class ArrayMultiplier:
    def __init__(self, array1, array2):
        if len(array1) != len(array2):
            raise ValueError("Arrays must be of equal length")
        self.array1 = array1
        self.array2 = array2

    def multiply_arrays(self):
        result = []
        for i in range(len(self.array1)):
            result.append(self.array1[i] * self.array2[i])
        return result

    def print_multiplication(self):
        result = self.multiply_arrays()
        print(*result, end=" ")


# Example usage
if __name__ == "__main__":
    a = [2, 3]
    b = [5, 4]
    multiplier = ArrayMultiplier(a, b)
    multiplier.print_multiplication()
