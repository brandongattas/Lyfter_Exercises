# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.

class Circle:
    radius=0

    def get_area(self):
        print(f"Circle area is: {3.1416*self.radius**2}")

my_circle = Circle()
my_circle.radius=25
my_circle.get_area()