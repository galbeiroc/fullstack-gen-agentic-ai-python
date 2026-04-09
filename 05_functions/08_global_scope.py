order_type = "Burger" # Global scope

def front_desk():
  def kitchen():
    global order_type
    order_type = "Pasta"
  kitchen()

front_desk()
print(f"Global variable: {order_type}")