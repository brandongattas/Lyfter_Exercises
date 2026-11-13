# 1. Cree una estructura de objetos que asemeje un Stack.
#     -Debe incluir los métodos de push (para agregar nodos) y 
#      pop (para quitar nodos).
#     -Debe incluir un método para hacer print de toda la estructura.
#     -No se permite el uso de tipos de datos compuestos como lists, 
#      dicts o tuples ni módulos como collections.

class StackEmptyError(Exception):
    pass

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def push(self, new_node):
        current_node = self.head
        self.head = new_node
        new_node.next = current_node

    def pop(self):
        if self.head is None:
            raise StackEmptyError("[ERROR] The Stack is Empty.")

        current_node = self.head
        self.head = self.head.next
        return current_node.data

    def print_stack(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

stack = Stack()

stack.push(Node("First Node"))
stack.push(Node("Second Node"))
stack.push(Node("Third Node"))

stack.print_stack()

print("Removed: ", stack.pop())
stack.print_stack()

try:
    stack.pop()
    stack.pop()
    stack.pop()
except StackEmptyError as e:
    print(e)