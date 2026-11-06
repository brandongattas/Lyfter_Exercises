# 2. Cree una clase abstracta User con los siguientes 
# métodos abstractos:
#     get_role()
#     has_permission(permission)
# Luego cree dos clases que hereden de ella:
#     AdminUser
#     RegularUser
# Cada una debe implementar los métodos
# Por ejemplo:
#     AdminUser siempre tiene permisos
#     RegularUser solo tiene permisos limitados ("read", por ejemplo)
# Ejemplo:
#     Entrada:
#         user1 = AdminUser("Carlos")
#         user2 = RegularUser("Andrea")

#     Salida:
#         print(user1.has_permission("delete"))  # True
#         print(user2.has_permission("delete"))  # False

from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        allowed = ["read","write","delete"]
        return permission in allowed

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        allowed = ["read"]
        return permission in allowed


user1 = AdminUser("Brandon")
user2 = RegularUser("Mohammed")

print(f"Does user: {user1.name} with role: {user1.get_role()}, has permission to delete?: {user1.has_permission('delete')}")
print(f"Does user: {user2.name} with role: {user2.get_role()}, has permission to delete?: {user2.has_permission('delete')}")