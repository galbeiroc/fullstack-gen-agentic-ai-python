drink_menu = { "coffee": 25, "tea": 20 }

try:
  drink_menu["lemonade"]
except KeyError:
  print("The key that you are trying to access doesnt exits")

print("Drink code")