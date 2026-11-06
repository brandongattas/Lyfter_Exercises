# Cree una función que se llame multiply, la cual obtiene dos valores 
# y los multiplica entre si
# -A esta función se le debe combinar dos decoradores:
#   @log_call: imprime el nombre de la función, los argumentos, 
#       fecha actual y el retorno
#   @validate_numbers: revisa que todos los argumentos sean numéricos
# Ejemplo:
    
# Entrada:
#     multiply(3, 4)

# Salida:
#     "func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
#     "Resultado 12"


from functools import wraps
from datetime import datetime

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        today_date = datetime.now()
        func_name = func.__name__
        result = func(*args, **kwargs)

        print(f"func:{func_name} - args: {args} - kwargs:{kwargs} - [{today_date}] - Result: {result}")

        return result
    
    return wrapper

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All the values must be numeric.")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("All the values must be numeric.")
            
        return func(*args, **kwargs)
    
    return wrapper


@validate_numbers
@log_call
def multiply(n1, n2):
    print("Executing....")
    return n1*n2

try:
    multiply(5, "5")
except ValueError as e:
    print(e)