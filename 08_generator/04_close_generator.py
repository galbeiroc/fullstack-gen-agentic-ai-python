def local_drink():
  yield "Coffee"
  yield "Tea"

def imported_drink():
  yield "Capuchino"
  yield "Ice Tea"

def full_drink_menu():
  yield from local_drink()
  yield from imported_drink()

for drink in full_drink_menu():
  print(drink)

def coffee_stall():
  try:
    while True:
      yield "Waiting for Coffee order"
  except GeneratorExit:
    print("Stall closed!")

stall = coffee_stall()
print(next(stall)) # Starts generator, prints "Waiting for Coffee order"

stall.close() #cleanup