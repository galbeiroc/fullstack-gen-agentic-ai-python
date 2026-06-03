def serve_drink():
  drink_type = "Soda" #. Local scope
  print(f"Inside Serving {drink_type}...")

drink_type = "Water"
serve_drink()
print(f"Outside Serving {drink_type}...")


def drink_counter():
  drink_ordered = "Lemonade" # Enclosing scope
  def print_order():
    drink_ordered = "Juice"
    print(f"Inner function: {drink_ordered}")
  print_order()
  print(f"Outer function: {drink_ordered}")

drink_ordered = "Beer" # Global scope
drink_counter()
print(f"Global variable: {drink_ordered}")