# Cree una clase Product con:
# Nombre, precio y cantidad
# -Cree una clase Inventory que:
#       -Guarde productos en una lista
#       -Tenga métodos para:
#           -Agregar un producto
#           -Mostrar todos los productos
#           -Calcular el valor total del inventario
# Ejemplo:
#     Entrada:
#         product1 = Product("Mouse", 5000, 3)
#         product2 = Product("Teclado", 8000, 2)

#     Salida:
#         print(product.calculate_total_value_of_inventory) #34000

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory():
    def __init__(self):
        self.products_list=[]

    def add_product(self, product):
        self.products_list.append(product)

    def view_all_products(self):
        for product in self.products_list:
            print(f"Name: {product.name} | Price: {product.price} | Quantity: {product.quantity}")

    def view_total_inventory_value(self):
        total_value=0
        for product in self.products_list:
            total_value+=product.price*product.quantity
        return total_value

my_inventory = Inventory()

product_1 = Product("Mouse", 100, 3)
product_2 = Product("Laptop", 3000, 15)
product_3 = Product("Keyboard", 200, 14)

my_inventory.add_product(product_1)
my_inventory.add_product(product_2)
my_inventory.add_product(product_3)

my_inventory.view_all_products()

print("Total inventory value: ",my_inventory.view_total_inventory_value())