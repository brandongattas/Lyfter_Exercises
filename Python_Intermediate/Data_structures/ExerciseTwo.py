# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     -Debe incluir los métodos de push_left y push_right (para agregar 
#      nodos al inicio y al final) y pop_left y pop_right (para quitar 
#      nodos al inicio y al final).
#     -Debe incluir un método para hacer print de toda la estructura.
#     -No se permite el uso de tipos de datos compuestos como lists, 
#      dicts o tuples ni módulos como collections.

class DequeueEmptyError(Exception):
	pass

class Node:
	data: str
	next: "Node"
	prev: "Node"

	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class Deque:
	def __init__(self):
		self.head = None
		self.tail = None

	def push_right(self, new_node):
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

	def push_left(self, new_node):
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def pop_left(self):
		if self.head is None:
			raise DequeueEmptyError("[ERROR] Dequeue is Empty!")

		removing_node = self.head
		self.head = self.head.next
		if self.head is not None:
			self.head.prev = None
		else:
			self.tail=None
		return removing_node.data

	def pop_right(self):
		if self.tail is None:
			raise DequeueEmptyError("[ERROR] Dequeue is Empty!")

		removing_node = self.tail
		self.tail = self.tail.prev
		if self.tail is not None:
			self.tail.next = None
		else:
			self.head=None
		return removing_node.data

	def print_dequeue(self):
		current = self.head

		while current is not None:
			print(current.data, end="")

			if current.next is not None:
				print(" <-> ", end="")

			current = current.next

		print()

deque = Deque()

deque.push_right(Node("A"))
deque.push_right(Node("B"))
deque.push_right(Node("C"))
deque.push_left(Node("Z"))
deque.push_left(Node("Y"))

deque.print_dequeue()

print("Removing from left: ", deque.pop_left())
deque.print_dequeue()

print("Removing from right: ", deque.pop_right())
deque.print_dequeue()

try:
	print("Removing from right: ", deque.pop_right())
	deque.print_dequeue()
	print("Removing from left: ", deque.pop_left())
	deque.print_dequeue()
	print("Removing from right: ", deque.pop_right())
	deque.print_dequeue()
	print("Removing from right: ", deque.pop_right())
	deque.print_dequeue()
except DequeueEmptyError as e:
	print(e)