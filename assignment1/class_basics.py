class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle(self.width + other.width, self.height + other.height)

# Example usage
if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    r2 = Rectangle(5, 6)
    print(r1)
    print(f"Area: {r1.area()}, Perimeter: {r1.perimeter()}")
    print(f"r1 == r2? {r1 == r2}")
    print(f"r1 < r2? {r1 < r2}")
    r3 = r1 + r2
    print(f"r3 (r1 + r2): {r3}")
