# 3. Cree una clase de User que:
# -Tenga un atributo de date_of_birth.
# -Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User 
# como parámetro que se encargue de revisar si el User es mayor 
# de edad y arroje una excepción de no ser así.

from datetime import date
class User:
    def __init__(self, name, date_of_birth):
        self.date_of_birth = date_of_birth
        self.name = name

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age

def adults_only(func):
    def wrapper(user):
        print(f"Attempting operation for: {user.name} with age: {user.age}")
        if user.age < 18:
            raise ValueError(f"[ERROR] {user.name}, you must be an adult for this operation.")
        return func(user)

    return wrapper

@adults_only
def buy_alcohol(user):
    return f"Alcohol purchase for {user.name}, completed!"

adult_user = User("Brandon", date(1989, 6, 14))
minor_user = User("Bishara", date(2020, 6, 14))

print("")
print("### Alcohol purchase service ###")
print("")

print(buy_alcohol(adult_user))
print("")

try:
    print(buy_alcohol(minor_user))
except ValueError as e:
    print(e)