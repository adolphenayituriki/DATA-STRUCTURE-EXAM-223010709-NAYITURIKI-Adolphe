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


def my_stack():
      print("Order 001: Table")
      print("Order 002: Bed")
      print("Order 003: Desk")
      print("Order 004: Window")
      print("Order 005: Chair")
      print("Order 006: Storage unit")


if __name__ == "__main__":
    print("STACK FOR CUSTOMIZED FURNITURE DESIGN AND ORDER SYSTEM PROCESSING\n_________________________________________________________________")
    print("Available Orders (In Stack):\n")
    
    # Initialize the stack
    order_stack = Stack()
    
    # Push orders to the stack
    order_stack.push("Order 001: Table")
    order_stack.push("Order 002: Bed")
    order_stack.push("Order 003: Desk")
    order_stack.push("Order 004: Window")
    order_stack.push("Order 005: Chair")
    order_stack.push("Order 006: Storage unit")

    # Display stack content using a predefined function
    my_stack()

    # Demonstrate stack operations
    print("\nStack Operations:\n")
    print("Top of Stack:", order_stack.peek())
    print("Popped:", order_stack.pop())
    print("Top of Stack After Pop:", order_stack.peek())
    print("Popped:", order_stack.pop())
    print("Popped:", order_stack.pop())
    print("Is Stack Empty?", order_stack.is_empty())
