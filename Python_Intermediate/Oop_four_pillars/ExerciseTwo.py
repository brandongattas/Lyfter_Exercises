# 2. Cree una clase abstracta de Shape que:
#       -Tenga los métodos abstractos de calculate_perimeter y 
#        calculate_area.
#       -Ahora cree las siguientes clases que hereden de Shape e 
#        implementen esos métodos: Circle, Square y Rectangle.
#       -Cada una de estas necesita los atributos respectivos para 
#        poder calcular el área y el perímetro.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        #Implement this method to calculate perimeter to different shapes.
        pass

    @abstractmethod
    def calculate_area(self):
        #Implement this method to calculate area to different shapes.
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius=radius

    def calculate_perimeter(self):
        return 2 * 3.1416 * self.__radius

    def calculate_area(self):
        return 3.1416 * self.__radius**2

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Radius must be a positive number!")
        self.__radius = new_radius


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.__side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, new_side_length):
        if new_side_length <= 0:
            raise ValueError("Side length must be a positive number!")
        self.__side_length = new_side_length


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def calculate_area(self):
        return self.__length * self.__width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, new_length):
        if new_length <= 0:
            raise ValueError("Length must be a positive number!")
        self.__length = new_length

    def set_width(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be a positive number!")
        self.__width = new_width


my_circle = Circle(25)
print(f"My circle's perimeter is: {my_circle.calculate_perimeter():.2f}")
print(f"My circle's area is: {my_circle.calculate_area():.2f}")
print(f"Current radius is: {my_circle.get_radius()}")
my_circle.set_radius(33)
print(f"My circle's radius is now: {my_circle.get_radius()}")
print(f"My new circle's perimeter is: {my_circle.calculate_perimeter():.2f}")
print(f"My new circle's area is: {my_circle.calculate_area():.2f}")
print("")

my_square = Square(25)
print(f"My square's perimeter is: {my_square.calculate_perimeter():.2f}")
print(f"My square's area is: {my_square.calculate_area():.2f}")
print(f"My square's current side length is: {my_square.get_side_length()}")
my_square.set_side_length(33)
print(f"My square's side length is now: {my_square.get_side_length()}")
print(f"My square's perimeter is: {my_square.calculate_perimeter():.2f}")
print(f"My square's area is: {my_square.calculate_area():.2f}")
print("")


my_rectangle = Rectangle(25, 35)
print(f"My rectangle's perimeter is: {my_rectangle.calculate_perimeter():.2f}")
print(f"My rectangle's area is: {my_rectangle.calculate_area():.2f}")
print(f"My rectangle's current length is: {my_rectangle.get_length()}")
print(f"My rectangle's current width is: {my_rectangle.get_width()}")
my_rectangle.set_length(36)
my_rectangle.set_width(48)
print(f"My rectangle's length is now: {my_rectangle.get_length()}")
print(f"My rectangle's width is now: {my_rectangle.get_width()}")
print(f"My rectangle's perimeter is: {my_rectangle.calculate_perimeter():.2f}")
print(f"My rectangle's area is: {my_rectangle.calculate_area():.2f}")