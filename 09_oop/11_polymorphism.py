# Duck-typing
class Duck:
  def swim(self):
    print("The Ducks is swimming!")

class Albatross:
  def swim(self):
    print("The Albatross is swimming!")

birds = [Duck(), Albatross()]

for bird in birds:
  bird.swim()

# Overriding
class Animal:
  def speak(self):
    print("Animals speak")

class Dog(Animal):
  def speak(self):
    print("Woof, woof")

class Cat(Animal):
  def speak(self):
    print("Meow, meow")

def make_animal_speak(animal: Animal):
  animal.speak()

dog = Dog()
cat = Cat()
make_animal_speak(dog)
make_animal_speak(cat)