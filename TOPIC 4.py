class Node:
      def __init__(self, data):
            self.data = data
            self.next = None

class CircularLinkedList:
      def __init__(self):
            self.head = None

      def append(self, data):
            new_node = Node(data)
            if not self.head:
                  self.head = new_node
                  self.head.next = self.head
            else:
                  temp = self.head
                  while temp.next != self.head:
                        temp = temp.next
                  temp.next = new_node
                  new_node.next = self.head

      def display(self):
            if not self.head:
                  print("No orders.")
                  return
            temp = self.head
            while True:
                  print(temp.data, end=" -> ")
                  temp = temp.next
                  if temp == self.head:
                        break
            print()


if __name__ == "__main__":
      print("CIRCULAR LINKED LIST\n____________________")
      recent_orders = CircularLinkedList()
      recent_orders.append("Order 001: Table")
      recent_orders.append("Order 002: Bed")
      recent_orders.append("Order 003: Desk")
      recent_orders.append("Order 004: Window")
      recent_orders.append("Order 005: Chair")
      recent_orders.append("Order 006: Storage unit")

      print("Fixed Recent Orders:")
      recent_orders.display()
