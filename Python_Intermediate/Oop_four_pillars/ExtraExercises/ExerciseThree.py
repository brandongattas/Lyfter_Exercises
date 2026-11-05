# 1. Cree una clase base Vehicle con los atributos:
#     _brand
#     _year
# Agregue un método get_info() que devuelva una descripción del vehículo.
# Luego cree dos clases hijas:
#     Car
#     Motorcycle
# Cada una debe agregar su propio atributo (por ejemplo, doors o type) 
# y sobrescribir el método get_info() para incluir esta información adicional.
# Ejemplo:
#     Entrada:
#         vehicle1 = Car("Toyota", 2020, 4)
#         vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

#     Salida:
#         print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
#         print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva

class Vehicle():
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"

class Car(Vehicle):
    def __init__(self, brand, year, model, wheels):
        super().__init__(brand, year)
        self._model = model
        self._wheels = wheels

    def get_info(self):
        return f"{super().get_info()} - Model: {self._model} {self._wheels} wheels."

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type, wheels):
        super().__init__(brand, year)
        self._type = type
        self._wheels = wheels

    def get_info(self):
        return f"{super().get_info()} - Type: {self._type} {self._wheels} wheels."

vehicle1 = Car("Toyota", 2026, "Sienna", 4)
vehicle2 = Motorcycle("Yamaha", 2026, "Sports", 2)

print(vehicle1.get_info())
print(vehicle2.get_info())