# 11. Abstract Class
# Concept: Cannot be instantiated, only subclassed
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(AbstractShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
