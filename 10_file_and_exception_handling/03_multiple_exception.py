def process_order(item, quantity):
  try:
    price = { "coffee": 20, "ginger": 15 }[item]
    cost = price * quantity
    print(f"Total cost is {cost}")
  except KeyError:
    print("Sorry that drink is not on menu")
  except TypeError:
    print("Quantity must be a number")

process_order("lemonade", 2)
process_order("coffee", bool)