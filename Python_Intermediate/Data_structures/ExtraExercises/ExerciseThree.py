# 3. Lista doblemente enlazada
# Requisitos:
# Cada nodo debe tener referencia al siguiente y al anterior
# Métodos:

#     -append(data): Agrega al final
#         Ejemplo:
#         Entrada:
#             dll.append("A")
#             dll.append("B")
#             dll.append("C")
#         Salida (print_forward):
#             A -> B -> C
#         Salida (print_bacward):
#             C -> B -> A

#     -prepend(data): Agrega al inicio
#         Ejemplo:
#         Entrada:
#             dll.prepend("X")
#         Salida(print_forward):
#             X -> A -> B -> C
#         Salida(print_backward):
#             C -> B -> A -> X

#     -delete(data): Elimina el primer nodo con ese valor
#         Ejemplo:
#         Entrada:
#             dll.delete("B")
#         Salida(print_forward):
#             X -> A -> C
#         Salida(print_backward):
#             C -> A -> X

#     -print_forward() y print_backward(): Imprime en ambas direcciones
#         Ejemplo:
#         Salida:
#             print_forward()  #→ X -> A -> C
#             print_backward() #← C -> A -> X


class Node:
    data: str
    next: "Node | None"
    prev: "Node | None"

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head

        if current is None:
            return

        while current is not None:

            if current.data == data:

                if current.prev is None:
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                    else:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next is not None:
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev

                current.next = None
                current.prev = None

                return

            current = current.next

    def print_forward(self):
        current = self.head

        if current is None:
            return
        
        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

    def print_backward(self):
        current = self.tail

        if current is None:
            return

        while current is not None:
            print(current.data, end="")

            if current.prev is not None:
                print(" -> ", end="")

            current = current.prev

        print()

dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.prepend("X")

dll.delete("B")

dll.print_forward()
dll.print_backward()