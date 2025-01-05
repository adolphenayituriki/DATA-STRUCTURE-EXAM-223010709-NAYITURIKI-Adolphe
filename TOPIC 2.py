# Stack Implementation
class Stack:
      def __init__(self):
            self.stack = []

      def push(self, item):
            self.stack.append(item)

      def pop(self):
            return self.stack.pop() if not self.is_empty() else "Stack is empty"

      def peek(self):
            return self.stack[-1] if not self.is_empty() else "Stack is empty"

      def is_empty(self):
            return len(self.stack) == 0


# Binary Search Tree Implementation
class TreeNode:
      def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

class BST:
      def __init__(self):
            self.root = None

      def insert(self, data):
            if not self.root:
                  self.root = TreeNode(data)
            else:
                  self._insert(self.root, data)

      def _insert(self, node, data):
            if data < node.data:
                  if node.left:
                        self._insert(node.left, data)
                  else:
                        node.left = TreeNode(data)
            else:
                  if node.right:
                        self._insert(node.right, data)
                  else:
                        node.right = TreeNode(data)


      def inorder(self, node):
            if node:
                  self.inorder(node.left)
                  print(node.data, end=" -> ")
                  self.inorder(node.right)

def my_stack():
            order = "Order 001: Table\nOrder 002: Bed\nOrder 003: Desk\nOrder 004: Window\nOrder 005: Chair\nOrder 006: Storage unit\n"
            print(order)
if __name__ == "__main__":
# Stack Example
      print("STACK FOR CUSTOMIZED FURNITURE DESIGN AND ORDER SYSTEM\n______________________________________________________")
      print("Available Furniture Orders (In Stack):")
      my_stack()
      order_stack = Stack()
      order_stack.push("Order 001: Table")
      order_stack.push("Order 002: Bed")
      order_stack.push("Order 003: Desk")
      order_stack.push("Order 004: Window")
      order_stack.push("Order 005: Chair")
      order_stack.push("Order 006: Storage unit")

      print("Top of Stack:", order_stack.peek())
      print("Popped:", order_stack.pop())
      print("Top of Stack After Pop:", order_stack.peek())
      print()




# BST Example
      print("BINARY SEARCH TREE (BST)\n_________________________")
      bst = BST()
      orders = [30, 25, 40, 20, 38, 35, 45]
      for order in orders:
            bst.insert(order)
      print("Inorder Traversal (Sorted Orders):")
      bst.inorder(bst.root)
      print()
