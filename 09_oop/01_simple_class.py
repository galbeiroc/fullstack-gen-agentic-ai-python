class Drink:
  pass

class DrinkTime:
  pass

print(type(Drink))

tea_drink = Drink()
print(type(tea_drink))
print(type(tea_drink) is Drink)
print(type(tea_drink) is DrinkTime)
