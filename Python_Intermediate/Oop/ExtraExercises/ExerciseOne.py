# Cree una clase Rectangle que:
#     -Tenga atributos width y height
#     -Tenga un método get_area() que retorne el área
#     -Tenga un método get_perimeter() que retorne el perímetro
#     -Valide que ningún valor sea negativo. Si lo es, lance una 
#      excepción con un mensaje adecuado

# Ejemplo 1:
#     Entrada:
#         "Ingrese la altura: " 250
#         "Ingrese el ancho: " 300

#     Salida:
#         print(rectangle.get_area()) #75000
#         print(rectangle.get_perimeter()) #1100

class Rectangle():

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Neither width nor height can be negative numbers.")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

try:
    user_width = int(input("Enter the rectangle's width: "))
    user_height = int(input("Enter the rectangle's height: "))

    my_rectangle = Rectangle(user_width, user_height)
    
    print(f"My rectangle's area is: {my_rectangle.get_area()}")
    print(f"My rectangle's perimeter is: {my_rectangle.get_perimeter()}")

except ValueError as e:
    print(e)