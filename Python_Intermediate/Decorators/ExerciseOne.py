# Cree un decorador que haga print de los parámetros 
# y retorno de la función que decore.

from functools import wraps

def print_parameters(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print("Printing parameters from wrapper.")
		for arg in args:
			print(arg)

		for key, value in kwargs.items():
			print(f"{key}={value}")

		result = func(*args, **kwargs)
		print(f"Return result: {result}")
		return result

	return wrapper

@print_parameters
def calculate_addition(num1, num2):
	return num1+num2

print(f"Addition result using kwargs: {calculate_addition(num1=25, num2=30)}")
print(f"Addition result using args: {calculate_addition(25, 30)}")