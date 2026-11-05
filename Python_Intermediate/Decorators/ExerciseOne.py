# Cree un decorador que haga print de los parámetros 
# y retorno de la función que decore.

def print_parameters(func):
    def wrapper(*args):
        print("Printing parameters from wrapper.")
        for arg in args:
            print(arg)

        return func(*args)

    return wrapper

@print_parameters
def calculate_addition(num1, num2):
    return num1+num2

print(f"Addition result: {calculate_addition(25, 30)}")