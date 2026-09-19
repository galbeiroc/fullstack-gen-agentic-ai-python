class OutOfIngredientsError(Exception):
  def __init__(self, message):
    self.message = message

def make_coffee(milk, sugar):
  if milk == 0 or sugar == 0:
    raise OutOfIngredientsError("Sugar or milk are missing!")
  print("Coffee Ready...")

make_coffee(0, 2)