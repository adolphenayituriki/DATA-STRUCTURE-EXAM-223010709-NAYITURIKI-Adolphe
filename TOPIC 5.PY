class BinaryTreeNode:
      def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

class BinaryTree:
      def __init__(self):
            self.root = None

      def insert_left(self, node, data):
            if not node.left:
                  node.left = BinaryTreeNode(data)
            else:
                  print("Left child already exists.")

      def insert_right(self, node, data):
            if not node.right:
                  node.right = BinaryTreeNode(data)
            else:
                  print("Right child already exists.")

      def display(self, node, level=0):
            if node:
                  self.display(node.right, level + 1)
                  print("  " * level, node.data)
                  self.display(node.left, level + 1)


if __name__ == "__main__":
      print("BINARY TREE\n____________")
      tree = BinaryTree()
      tree.root = BinaryTreeNode("Order 001: Table")
      tree.insert_left(tree.root, "Order 002: Bed")
      tree.insert_right(tree.root, "Order 003: Desk")
      child = BinaryTree()
      tree.child = BinaryTreeNode("Order 001: Window")
      tree.insert_left(tree.child, "Order 002: Chair")
      tree.insert_right(tree.child, "Order 003: Storage Unit")

      print("Binary Tree to track data dynamically in customized furniture design and order system:\n")
      tree.display(tree.root)
      tree.display(tree.child)
