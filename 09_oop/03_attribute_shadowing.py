class Employee:
  name = "Jhon"
  lastname = "Doe"

employee = Employee()
print(employee.name)

# Shadowing the class attribute
employee.name = "Sam"
employee.age = 32
print("After changing ", employee.name)
print("Direct look into the class", Employee.name)

del employee.name
del employee.age
print(employee.name)
print(employee.age) #AttributeError: 'Employee' object has no attribute 'age'