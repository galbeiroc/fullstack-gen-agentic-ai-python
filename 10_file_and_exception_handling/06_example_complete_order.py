class InvalidDrinkError(Exception):
  pass

def bill(flavor, cups):
  menu = { "coffee": 20, "lemonade": 24, "tea": 15 }
  try:
    if flavor not in menu:
      raise InvalidDrinkError("That drink is not available")
    if not isinstance(cups, int):
      raise TypeError("Cups must be an integer")
    total = menu[flavor] * cups
    print(f"Your bills for {cups} cups of {flavor} drink: usd {total}")
  except Exception as e:
    print("Error: ", e)
  finally:
    print('Thanks you for visiting our cafe')

bill("chocolate", 2)
bill("coffee", "three")
bill("coffee", 3)