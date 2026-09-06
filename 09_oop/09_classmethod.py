class DrinkOrder:
  def __init__(self, drink_type, sweetness, size):
    self.drink_type = drink_type
    self.sweetness = sweetness
    self.size = size

  @classmethod
  def from_dict(cls, order_data):
    return cls(
      order_data["drink_type"],
      order_data["sweetness"],
      order_data["size"]
    )

  @classmethod
  def from_string(cls, order_string):
    drink_type, sweetness, size = order_string.split(",")
    return cls(drink_type, sweetness, size)

order1 = DrinkOrder.from_dict({ "drink_type": "Coffee", "sweetness": "low", "size": "medium" })

print(order1.__dict__)
print(order1.size)

order2 = DrinkOrder.from_string("Tea, medium, small")
print(order2.__dict__)
print(order2.drink_type)