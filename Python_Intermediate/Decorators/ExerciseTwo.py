# 2. Cree un decorador que se encargue de revisar si todos los 
# parámetros de la función que decore son números, y arroje una 
# excepción de no ser así.

def check_if_parameters_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("[ERROR] All the parameters values must be integers.")
            
        print("Validated - All parameter values are Ok!")
        return func(*args)
        
    return wrapper

@check_if_parameters_int
def addition(n1, n2, n3, n4):
    return n1+n2+n3+n4

print(f"Addition result: {addition(1,2,3,4)}")
print(f"Addition result: {addition(1,2,"ab",3)}")