value = 14
""" remainder = value % 5

if remainder:
  print(f"Not divisible by 5, remainder is {remainder}") """

if (remainder := value % 5):
  print(f"Not divisible by 5, remainder is {remainder}")

print(f"Value is {value}, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (size := input("What size do you want? ")) in available_sizes:
  print(f"Great, we have {size} size available")
else:
  print(f"Sorry, we don't have {size} size available")


flavors = ["vanilla", "chocolate", "strawberry"]

while (flavor := input("What flavor do you want? ")) not in flavors:
  print(f"Sorry, {flavor} flavor is not available")

print(f"Great, we have {flavor} flavor available")
