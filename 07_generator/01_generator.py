def serve_drink():
  yield "Cup 1: Coffee"
  yield "Cup 2: Tea"
  yield "Cup 3: Chocolate"

drinks = serve_drink()

for cup in drinks:
  print(cup)

def get_cup_gen():
  yield "Cup 1"
  yield "Cup 2"
  yield "Cup 3"

cups = get_cup_gen()
print(next(cups))
print(next(cups))