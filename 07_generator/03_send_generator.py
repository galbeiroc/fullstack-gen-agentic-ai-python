def drink_customer():
  print("Welcome!, What drink do you like?")
  order = yield
  while True:
    print(f"Preparing {order}")
    order = yield

drinks = drink_customer()
next(drinks) # Start generator

drinks.send("Coffee")
drinks.send("Tea")