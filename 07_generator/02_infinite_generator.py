def infinite_counter(start=0, step=1):
  count = start
  while True:
    yield f"Count  #{count}"
    count += step

counter = infinite_counter()

numbers = infinite_counter()

for _ in range(3):
  print(next(counter))

for _ in range(6):
  print(next(numbers))
