# 2. Cree una clase LinkedList con los métodos:
#     -insert_front(data): Inserta al inicio
#     Ejemplo:
#         Entrada:
#             ll.insert_front(10)
#             ll.insert_front(20)
#         Salida:
#             20 -> 10
#     -insert_back(data): Inserta al final
#     Ejemplo:
#         Entrada:
#             ll.insert_back(30)
#         Salida:
#             20 -> 10 -> 30
#     -delete(data): Elimina el primer nodo con el valor dado
#     Ejemplo:
#         Entreada:
#             ll.delete(10)
#         Salida:
#             20 -> 30
#     -print_all(): Imprime todos los valores
#     Ejemplo:
#         Salida:
#             ll.print_all() #20 -> 30

class Node:
    data: int
    next: "Node | None"

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def delete(self, data):
        current = self.head
        previous = None

        while current is not None:

            if current.data == data:

                if previous is None:
                    self.head = self.head.next
                else:
                    previous.next = current.next

                return

            previous = current
            current = current.next

    def print_all(self):
        current = self.head

        if current is None:
            return
        
        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)

ll.print_all()

ll.insert_back(30)
ll.insert_back(40)

ll.print_all()

ll.delete(30)
ll.print_all()

ll.delete(20)
ll.print_all()