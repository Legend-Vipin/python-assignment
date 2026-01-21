# 12. Concrete Class
# Concept: Can be instantiated, implements all abstract methods
class ConcreteShape:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def describe(self):
        return f"{self.name} has an area of {self.area}."

circle = ConcreteShape("Circle", 78.5)
square = ConcreteShape("Square", 16)

print(circle.describe())
print(square.describe())
