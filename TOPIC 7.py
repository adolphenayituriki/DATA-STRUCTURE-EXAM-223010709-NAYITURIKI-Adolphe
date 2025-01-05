def bubble_sort(orders):
      n = len(orders)
      for i in range(n):
            for j in range(n - i - 1):
                  if orders[j]['Option'] > orders[j + 1]['Option']:
                        orders[j], orders[j + 1] = orders[j + 1], orders[j]

if __name__ == "__main__":
      print("BUBBLE SORT BY OPTIONS\n______________________")
      order_list = [
            {'order_id': 1, 'Option': 3},
            {'order_id': 2, 'Option': 1},
            {'order_id': 3, 'Option': 4},
            {'order_id': 4, 'Option': 2},
            {'order_id': 5, 'Option': 6},
            {'order_id': 6, 'Option': 5}
]

      print("\nORDERS BEFORE SORTING:\n")
      for x in order_list:
            print(x)

      bubble_sort(order_list)

      print("\nORDERS AFTER SORTING BY OPTION:\n")
      for y in order_list:
            print(y)
