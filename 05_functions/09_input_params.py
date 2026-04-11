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

# *args
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("galbeiroc", "Tobias", "Emir")

# **kwargs
def my_function(**kwargs):
  print("Type:", type(kwargs))
  print("Name:", kwargs["name"])
  print("Age:", kwargs["age"])
  print("All keyword arguments:", kwargs)

my_function(name="galbeiroc", age=30, city="New York")