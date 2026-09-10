class Employee:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.address = None # Composite Attr

  def describe(self):
    print(f"{self.name} is responsible and kind!")

class SalaryEmployee(Employee):
  def __init__(self, id, name, weekly_salary):
    super().__init__(id, name)
    self.weekly_salary = weekly_salary

  def calculate_payroll(self):
    return self.weekly_salary

# Composition
class Address:
  def __init__(self, street, city, state, zipcode):
    self.street = street
    self.city = city
    self.state = state
    self.zipcode = zipcode

  def __str__(self):
    lines = [self.street]
    lines.append(f"{self.city}, {self.state}, {self.zipcode}")

    return "\n".join(lines)


address = Address("55 Main St.", "Concord", "NH", "03301")
jhon = Employee(10, "Jhon")
jhon.address = address
print(jhon.address)