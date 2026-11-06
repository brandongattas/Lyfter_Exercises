# 1. Cree una clase Employee con los siguientes requisitos:
#     Atributos privados: _name, _salary
#     Use @property y @<atributo>.setter para:
#     Mostrar el nombre y el salario
#     Validar que el salario nunca sea negativo
#     Cree un método promote que aumente el salario un porcentaje definido
#     Ejemplo:
#         Entrada:
#             employee = Employee("Ana", 1000)
#             employee.promote(0.1)  # +10%

#         Salida:
#             print(employee.salary)  # 1100

class Employee():
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name or not new_name.strip():
            raise ValueError("[ERROR] name cannot be empty.")
        if any(char.isdigit() for char in new_name):
            raise ValueError("[ERROR] name cannot contain numbers.")
        self._name = new_name.strip()
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("[ERROR] The salary must be a positive number.")
        self._salary = new_salary

    def promote(self, raise_rate):
        if raise_rate <= 0:
            raise ValueError("[ERROR] raise_rate cannot be negative.")
        self._salary += (self._salary * raise_rate)

employee = Employee("Brandon", 12000)
print(employee.salary)
print(employee.name)
employee.promote(0.25)
print(employee.salary)
employee.salary = 16000
print(employee.salary)
employee.name = "Brandon Gattas"
print(employee.name)