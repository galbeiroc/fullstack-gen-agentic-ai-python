def get_name():
  return "galbeiroc"

my_name = get_name()
print(my_name)


def add_numbers(a, b):
  return a + b

result = add_numbers(5, 7)
print(result)

def make_coffee(cups_left):
  if cups_left == 0:
    return "No more coffee!"
  return "Here's your coffee!"

print(make_coffee(3))
print(make_coffee(0))

def report_coffee():
  return 100, 20, 10

total_cups, cups_left, _ = report_coffee()
print("Sold out:", total_cups)
print("Cups left:", cups_left)