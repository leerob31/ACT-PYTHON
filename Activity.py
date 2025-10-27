ACT 1: Animal Inheritance

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Create objects
dog = Dog()
cat = Cat()

# Call their methods
dog.speak()
cat.speak()

# Activity 2: Vehicle Class

# Parent class
class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

# Child class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, fuel, doors):
        # Call the parent class constructor using super()
        super().__init__(brand, fuel)
        self.doors = doors

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"Driving {self.brand}... Fuel left: {self.fuel}")
        else:
            print(f"{self.brand} has no fuel left!")

# Create an object of Car
car1 = Car("Toyota", 5, 4)

# Call the drive() method
car1.drive()
car1.drive()

Part 2
# Activity 1: Bank Account

class BankAccount:
    def __init__(self):
        # Private variable: cannot be accessed directly outside the class
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid or insufficient amount!")

    def get_balance(self):
        return self.__balance

 Activity 2: Age Validation

class Person:
    def __init__(self):
        self._age = 0   # Protected variable (single underscore)

    # Getter method — safely returns the age value
    @property
    def age(self):
        return self._age

Part3
 Activity 1: Printers

class InkPrinter:
    def print_document(self):
        print("Printing document using ink printer...")

class LaserPrinter:
    def print_document(self):
        print("Printing document using laser printer...")

# Demonstrating polymorphism
def show_print(printer):
    printer.print_document()

ink = InkPrinter()
laser = LaserPrinter()

show_print(ink)
show_print(laser)


You sent
# Activity 2: Duck Typing

def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Tweet tweet!")

class Robot:
    def speak(self):
        print("Beep boop!")

# Demonstration
bird = Bird()
robot = Robot()

make_it_speak(bird)
make_it_speak(robot)

Part 4
act 1:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Demonstration
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())

Act2:

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

# Demonstration
hourly = HourlyEmployee("John", 40, 150)
salaried = SalariedEmployee("Anna", 30000)

print(f"{hourly.name}'s Pay: ₱{hourly.calculate_pay()}")
print(f"{salaried.name}'s Pay: ₱{salaried.calculate_pay()}")
