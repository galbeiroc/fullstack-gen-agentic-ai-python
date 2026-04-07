users = [
  { "id": 1, "name": "Alice", "total": 100, "coupon": "DISCOUNT10" },
  { "id": 2, "name": "Bob", "total": 200, "coupon": "DISCOUNT20" },
  { "id": 3, "name": "Charlie", "total": 300, "coupon": "DISCOUNT30" }
]

discounts = {
  "DISCOUNT10": (0.10, 0),
  "DISCOUNT20": (0.20, 0),
  "DISCOUNT30": (0.30, 0)
}

for user in users:
  percentage, fixed = discounts.get(user['coupon'], (0, 0))
  discount_amount = user['total'] * percentage + fixed
  print(f"{user['name']} paid {user['total']} and got a discount of {discount_amount:.2f}")