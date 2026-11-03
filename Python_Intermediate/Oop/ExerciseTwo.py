# Cree una clase de Bus con:
#   -Un atributo de max_passengers.
#   -Un método para agregar pasajeros uno por uno 
#      (que acepte como parámetro una instancia de la clase 
#       Person vista en la lección). Este solo debe agregar pasajeros 
#       si lleva menos de su máximo. Sino, debe mostrar un mensaje de 
#       que el bus está lleno.
#   -Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person():
	def __init__(self, name):
		self.name = name
		print(f"Ha nacido una persona llamada {name}!")


class Bus():

	def __init__(self, max_passengers=0):
		self.max_passengers=max_passengers
		self.passenger_counter=0

	def board_passenger(self, passenger: Person):
		if self.passenger_counter < self.max_passengers:
			self.passenger_counter += 1
			print(f"Welcome to my bus, {passenger.name}!")
		else:
			print("The bus is full.")

	def alight_passenger(self, passenger: Person):
		if(self.passenger_counter > 0):
			self.passenger_counter -= 1
			print(f"Good bye, {passenger.name}, take care!")
		else:
			print("The bus is empty.")

person_1 = Person("John")
person_2 = Person("Marcela")
person_3 = Person("Miguel")
person_4 = Person("Juanito")

my_bus = Bus(max_passengers=3)

my_bus.board_passenger(person_1)
my_bus.board_passenger(person_2)
my_bus.board_passenger(person_3)
my_bus.board_passenger(person_4)

my_bus.alight_passenger(person_2)
my_bus.alight_passenger(person_4)
my_bus.alight_passenger(person_1)
my_bus.alight_passenger(person_3)