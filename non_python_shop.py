import sys
print(sys.version)

class Chai:
  def __init__(self, sweetness, milk_level):
    self.sweetness = sweetness
    self.milk_level = milk_level

  def sip(self):
    print("Sipping chai")

  def add_suggar(self, amount):
    print("Adding sugar", amount)


my_chai = Chai(sweetness=2, milk_level=6)
my_chai.sip()
my_chai.add_suggar(amount=10)

print(my_chai.sweetness)
print(my_chai.milk_level)