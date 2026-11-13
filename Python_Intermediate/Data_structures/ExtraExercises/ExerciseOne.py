# 1. Cree una estructura que represente una cola básica (Queue) con objetos enlazados
#       -Restricción: no usar list, dict, tuple, collections
# Métodos requeridos:
#
#     -enqueue(data): agrega un nodo al final
#         Ejemplo:
#             Entrada:
#                 q.enqueue("A")
#                 q.enqueue("B")
#                 q.enqueue("C")
#             Salida:
#                 A -> B -> C

#     -dequeue(): elimina y retorna el nodo del inicio
#         Ejemplo:
#             Entrada:
#                 q.dequeue()
#             Salida:
#                 "A"
#     -print_all(): imprime todos los elementos de la cola en orden
#         Ejemplo:
#             Entrada:
#                 q.print_all()
#             Salida:
#                 B -> C

class QueueEmptyError(Exception):
	pass

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise QueueEmptyError("[ERROR] The Queue is empty!")
        
        removing_node = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removing_node.data

    def print_queue(self):
        current = self.front

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")

queue.print_queue()

print("Removing from Queue: ", queue.dequeue())
queue.print_queue()

try:
    print("Removing from Queue: ", queue.dequeue())
    queue.print_queue()
    print("Removing from Queue: ", queue.dequeue())
    queue.print_queue()
    print("Removing from Queue: ", queue.dequeue())
    queue.print_queue()
    print("Removing from Queue: ", queue.dequeue())
except QueueEmptyError as e:
    print(e)