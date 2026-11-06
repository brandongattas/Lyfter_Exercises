# 1. Cree una función que imprima “Hola, [nombre]” dos veces:
# Cree un decorador @repeat_twice que haga que la función decorada 
# se ejecute dos veces seguidas, con los mismos argumentos
# Ejemplo:
#     Salida:
#         "Hola, Jeanca"
#         "Hola, Jeanca"

def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat_twice
def print_name(name):
    print(f"Hola, {name}")

print_name("Brandon")

@repeat_twice
def print_numbers(numbers_dict):
    print(f"Hola, {numbers_dict}")

print_numbers({"n1":1,"n2":2,"n3":3})