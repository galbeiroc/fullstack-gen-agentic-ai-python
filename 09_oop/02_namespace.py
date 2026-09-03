class Person:
  name = 'galbeiroc'

print(type(Person))

Person.age = 36

sam = Person()
sam.name = "Sam"
sam.age = 32

print(Person.name, Person.age)
print(sam.name, sam.age)