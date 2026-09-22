""" file = open("order.txt", "w")
try:
  file.write("Coffee drink - 2 Cups - 40 usd")
finally:
  file.close()
 """

# Modern way
with open("order.txt", "w") as file:
  file.write("Tea drink - 4 Cups - 20 usd")