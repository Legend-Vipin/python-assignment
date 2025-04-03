# 7. Access Modifiers (Python Conventions)
# Concept: Controlling visibility (Public, Protected _, Private __)
class Person:
    def __init__(self, name, age, secret):
        self.name = name
        self._age = age
        self.__secret = secret

    def display_public(self):
        print(f"Public Name: {self.name}")

    def _display_protected(self):
        print(f"Protected Age: {self._age}")

    def reveal_secret(self):
        print(f"Revealing Private Secret: {self.__secret}")

    def __internal_processing(self):
        print(f"Doing something private with {self.__secret}")

    def do_something_private(self):
        self.__internal_processing()

class Employee(Person):
    def __init__(self, name, age, secret, employee_id):
        super().__init__(name, age, secret)
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Age (Protected): {self._age}")

p = Person("Charlie", 30, "Loves chocolate")
emp = Employee("Dana", 25, "Wants a raise", "E123")

print("Accessing from outside the class:")
print(f"Public access: {p.name}")
print(f"Protected access (by convention, avoid): {p._age}")
try:
    print(p.__secret)
except AttributeError as e:
    print(f"Cannot access private attribute directly: {e}")

print("\nAccessing via methods:")
p.display_public()
p._display_protected()
p.reveal_secret()
p.do_something_private()

print("\nAccessing from subclass:")
emp.display_employee_info()
