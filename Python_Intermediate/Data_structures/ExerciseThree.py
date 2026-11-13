# 3. Cree una estructura de objetos que asemeje un Binary Tree.
# -Debe incluir un método para hacer print de toda la estructura.
# -No se permite el uso de tipos de datos compuestos como lists, 
#  dicts o tuples ni módulos como collections.

class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root=None

    def print_tree(self, node):
        if node is None:
            return

        print(node.data)
        self.print_tree(node.left)
        self.print_tree(node.right)

binary_tree = BinaryTree()

binary_tree.root = Node("A")
binary_tree.root.left = Node("B")
binary_tree.root.right = Node("C")
binary_tree.root.left.left = Node("D")
binary_tree.root.left.right = Node("E")
binary_tree.root.right.left = Node("F")
binary_tree.root.right.right = Node("G")

binary_tree.print_tree(binary_tree.root)