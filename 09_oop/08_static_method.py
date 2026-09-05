class Calculator:
  @staticmethod
  def add(a, b):
    """Returb the sum of two numbers"""
    return a + b

  @staticmethod
  def subtract(a, b):
    """Returns the difference between two numbers"""
    return a -b

print(Calculator.add(5, 9))
print(Calculator.subtract(17, 6))