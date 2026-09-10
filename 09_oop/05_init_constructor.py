class DrinkOrder:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def summary(self):
    return f"{self.size}ml of {self.name} drink."

coffee = DrinkOrder("Coffee", 200)
print(coffee.summary())
lemonade = DrinkOrder("Lemonade", 250)
print(lemonade.summary())