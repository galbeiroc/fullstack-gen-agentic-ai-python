def update_order():
  order_type = "Pizza"

  def kitchen():
    nonlocal order_type
    order_type = "Pasta"
    print(f"Inside Kitchen: {order_type}")

  kitchen()
  print(f"Outside Kitchen: {order_type}")

update_order()