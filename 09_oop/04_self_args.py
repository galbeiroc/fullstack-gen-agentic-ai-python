class Employee:
  name = "Jhon"

  def describe(self):
    return f"{self.name} is responsible and kind!"

jhon = Employee()
print(jhon.describe())

sam = Employee()
sam.name = "Sam"
print(sam.describe())