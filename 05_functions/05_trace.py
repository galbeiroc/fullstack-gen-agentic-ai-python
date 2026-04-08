def add_vat(price, vat_race):
  return price * (100 + vat_race) / 100

orders = [
  {"item": "Book", "price": 100},
  {"item": "Gadget", "price": 150},
  {"item": "Clothing", "price": 200}
]

for order in orders:
  amount = add_vat(order["price"], 10)
  print(f"Total price for {order['item']}: {amount}")