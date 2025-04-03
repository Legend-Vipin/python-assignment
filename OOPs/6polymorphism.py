# 6. Polymorphism
# Concept: Objects/methods taking multiple forms
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

def make_sound(animal_instance):
    print(f"{type(animal_instance).__name__} says: {animal_instance.speak()}")

dog = Dog()
cat = Cat()
duck = Duck()

make_sound(dog)
make_sound(cat)
make_sound(duck)

num1, num2 = 5, 10
str1, str2 = "Poly", "morphism"
list1, list2 = [1, 2], [3, 4]

print(f"{num1} + {num2} = {num1 + num2}")
print(f"'{str1}' + '{str2}' = {str1 + str2}")
print(f"{list1} + {list2} = {list1 + list2}")
