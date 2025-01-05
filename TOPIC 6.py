class TreeNode:
      def __init__(self, data):
            self.data = data
            self.children = []

      def add_child(self, child):
            self.children.append(child)

def display_tree(node, level=0):
      print("  " * level, node.data)
      for child in node.children:
            display_tree(child, level + 1)


if __name__ == "__main__":
      print("TREE TO REPRESENT HIERARCHICAL DATA\n____________________________________")
      root = TreeNode("Order 001: Table")
      furniture = TreeNode("Order 002: Bed")
      furniture.add_child(TreeNode("Order 003: Desk"))
      furniture.add_child(TreeNode("Order 004 : Window"))
      furniture.add_child(TreeNode("Order 005 : Chair"))
      furniture.add_child(TreeNode("Order 006 : Storage Unit"))
      root.add_child(furniture)

      print("A tree(order) to represent hierarchical data in the customized furniture design and order system:\n")
      display_tree(root)
