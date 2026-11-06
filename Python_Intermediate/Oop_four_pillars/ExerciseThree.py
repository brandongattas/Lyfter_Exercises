# 3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.


# Understanding Multiple Inheritance

# Multiple Inheritance occurs when a child class inherits directly from more than one parent class.
# While single inheritance represents an "is a" relationship (e.g., a Dog is an Animal), multiple inheritance is best used when an object naturally combines two completely different categories or skill sets.

# When should you use it?

# 1. Mixins: Creating small, specialized classes that add a single specific feature or behavior to other classes (e.g., adding a logging feature, database connectivity, or serialization to a standard data class).
# 2. Hybrid Objects: When an entity genuinely shares behaviors from distinct domains. For example, a Smartphone is both a Camera and a Phone.

# The Challenge/Risk: The Diamond Problem

# If two parent classes have a method with the exact same name, Python needs a way to decide which one to run first. Python solves this using MRO (Method Resolution Order), which reads parent classes from left to right.


#Parent Class 1
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"Driving the {self.brand} on the road."

#Parent Class 2
class Airplane:
    def fly(self):
        return "Flying high in the sky!"

#Child Class inheriting from BOTH Parent Classes
class FlyingCar(Car, Airplane):
    def __init__(self, brand):
        #We initialize the Car component
        super().__init__(brand) 



my_vehicle = FlyingCar("AeroCar")

#Inherited from Car
print(my_vehicle.drive())  #Output: Driving the AeroCar on the road.

#Inherited from Airplane
print(my_vehicle.fly())    #Output: Flying high in the sky!
