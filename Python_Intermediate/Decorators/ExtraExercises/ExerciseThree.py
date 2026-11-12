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

        args_string = ", ".join(repr(arg) for arg in args)

        kwargs_string = ", ".join(
                        f"{k}={repr(v)}" for k, v in kwargs.items()
                    )
        
        try:
            result = func(*args, **kwargs)
            
            print(f"func:{func_name} - args: {args_string} - kwargs:{kwargs_string} - [{today_date}] - Result: {result}")
            
            return result
        except Exception as e:
            print(f"func:{func_name} - args: {args_string} - kwargs:{kwargs_string} - [{today_date}] - FAILED: {e}")
            raise
    
    return wrapper

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, bool) or not isinstance(arg, (int, float)):
                raise TypeError("[ERROR] All the values must be numeric.")

        for value in kwargs.values():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("[ERROR] All the values must be numeric.")
            
        return func(*args, **kwargs)
    
    return wrapper


@log_call
@validate_numbers
def multiply(n1, n2):
    return n1*n2

print("------")
try:
    result = multiply(5, '5')
    print(f"Result {result}")
except TypeError as e:
    pass

print("")
print("------")
try:
    result = multiply(5, 5)
    print(f"Result {result}")
except TypeError as e:
    pass

print("")
print("------")
try:
    result = multiply(True, 5)
    print(f"Result {result}")
except TypeError as e:
    pass

print("")
print("------")
try:
    result = multiply(n1=5, n2=5)
    print(f"Result {result}")
except TypeError as e:
    pass

print("")
print("------")
try:
    result = multiply(n1=5, n2='5')
    print(f"Result {result}")
except TypeError as e:
    pass

print("")
print("------")
try:
    result = multiply(2.85, 5.25)
    print(f"Result {result}")
except TypeError as e:
    pass