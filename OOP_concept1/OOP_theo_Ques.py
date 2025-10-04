'''
Four Pillars of OOP
OOP is built on four fundamental pillars:

Encapsulation: Bundling data and methods within an object, providing data hiding 
and protection from external interference.
In Python, we achieve encapsulation using classes.

Abstraction: Hiding complex implementation details and exposing only relevant features. 
This allows us to focus on what an object does rather than how it does it. 
Abstract classes or interfaces in Python help achieve abstraction.

Inheritance: Creating hierarchies and allowing classes to inherit properties and methods from other classes.
It promotes code reuse and enables us to build a hierarchy of classes.
Python supports inheritance through base and derived classes.

Polymorphism: Enabling objects to take multiple forms. 
Objects can be treated as instances of their parent class or as instances of their child classes.
This promotes flexibility and extensibility in code.
In Python, polymorphism is achieved through method overriding and duck typing.

'''

# creating class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

#creating objects 
car1 = Car("Exter", "S plus", "2024")
car2 = Car("tesla", "Model X", "2025")
print(car1.display_info())

# Inheritance and Polymorphism in Action

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_life):
        # super().__init__() calls the parent class’s constructor so that the parent’s attributes (make, model, year) get initialized.
        super(). __init__( make, model, year)
        self.battery_life= battery_life

        def display_info(self):
        return f"{self.year} {self.make} {self.model} with {self.battery_capacity} kWh battery"

electric_car = ElectricCar("Nissan", "Leaf", 2023, 40)
 
print(electric_car.display_info())

