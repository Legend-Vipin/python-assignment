# 14. Static Methods / Attributes
# Concept: Belong to the class, not instances
class MathHelper:
    PI = 3.1415926535

    @staticmethod
    def calculate_circle_area(radius):
        if radius < 0:
            return 0
        return MathHelper.PI * (radius ** 2)

    @staticmethod
    def add(x, y):
        return x + y

print(f"Value of PI from class: {MathHelper.PI}")
print(f"Area of circle with radius 5: {MathHelper.calculate_circle_area(5)}")
print(f"Sum of 5 and 10: {MathHelper.add(5, 10)}")
