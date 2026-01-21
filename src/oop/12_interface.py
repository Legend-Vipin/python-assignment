# 13. Interface (Python uses Abstract Base Classes)
# Concept: Defines methods that must be created within any child classes
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Drawable):
    def draw(self):
        print("Drawing a rectangle.")

class Triangle(Drawable):
    def draw(self):
        print("Drawing a triangle.")

shapes = [Rectangle(), Triangle()]

for shape in shapes:
    shape.draw()
