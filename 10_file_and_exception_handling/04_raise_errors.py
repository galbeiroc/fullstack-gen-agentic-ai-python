def prepare_drink(drink):
  if drink not in ["Coffee", "Lemonade", "Tea"]:
    raise ValueError("Unsupported drink...")
  print(f"Preparing {drink} drink..")

prepare_drink("Pepsi")