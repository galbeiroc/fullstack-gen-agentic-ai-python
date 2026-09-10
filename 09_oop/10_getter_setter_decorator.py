# Using getter and setter
class Label:
  def __init__(self, text, font):
    self.text = text
    self.font = font

  def get_text(self):
    return self.text

  def set_text(self, text):
    self.text = text

  def get_font(self):
    return self.font

  def set_font(self, font):
    self.font = font

label = Label("Fruits", "Mono NL")
print(label.get_text())
label.set_text("Vegetables")
print(label.text)

# Using Property
class TeaLeaf:
  def __init__(self, age):
    self._age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, age):
    if 1 <= age <= 5:
      self._age = age
    else:
      raise ValueError("Tea leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 5
print(leaf.age)
