# 2. Cree un decorador que se encargue de revisar si todos los 
# parámetros de la función que decore son números, y arroje una 
# excepción de no ser así.

from functools import wraps

def check_if_parameters_is_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, bool) or not isinstance(arg, (int, float)):
                raise TypeError("[ERROR] All parameter values must be numbers.")
        
        for value in kwargs.values():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    "[ERROR] All parameter values must be numbers."
                )
        
        print("Validated - All parameter values are Ok!")
        return func(*args, **kwargs)
        
    return wrapper

@check_if_parameters_is_number
def addition(n1, n2, n3, n4):
    return n1+n2+n3+n4

try:
    print(f"Addition result: {addition(1,2,3,4)}")
except TypeError as e:
    print(e)

try:
    print(f"Addition result: {addition(1,2.5,3,4)}")
except TypeError as e:
    print(e)

try:
    print(f"Addition result: {addition(1,2,True,3)}")
except TypeError as e:
    print(e)

try:
    print(f"Addition result: {addition(1,2,'ab',3)}")
except TypeError as e:
    print(e)