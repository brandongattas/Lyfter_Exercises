# Cree un decorador @requires_login que:
# -Verifique si la variable global user_logged_in es True
# -Si no lo es, debe lanzar una excepción "Usuario no autenticado"
# -Si lo es, la función decorada se ejecuta normalmente
# Ejemplo:
#     Entrada:
#         user_logged_in = False

#         @requires_login
#         def view_profile():
#             print("Mostrando perfil del usuario")


from functools import wraps

class AuthenticationError(Exception):
    pass

user_logged_in=True

def requires_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise AuthenticationError("[ERROR] User not authenticated.")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("The user's profile is now visible.")

try:
    view_profile()
except AuthenticationError as e:
    print(e)

try:
    user_logged_in=False
    view_profile()
except AuthenticationError as e:
    print(e)