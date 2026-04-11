burger = "burger"

def prepare_meal(order):
  print(f"Preparing {order}...")

prepare_meal(burger)
print(f"{burger} is ready!")

num_orders = [1, 2, 3]

def update_orders(orders):
  orders[1] = 42 # This will modify the original list passed as an argument

update_orders(num_orders)
print(num_orders)

def make_pizza(size, cheese, toppings):
  print(f"Making a {size} pizza with {cheese} cheese and {toppings} toppings.")

make_pizza("large", "mozzarella", ["pepperoni", "mushrooms"]) # Positional arguments
make_pizza(size="medium", toppings=["olives", "onions"], cheese="cheddar") # Keyword arguments (order doesn't matter)
