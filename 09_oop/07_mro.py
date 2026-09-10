class A:
  label = "A: Base class"

class B(A):
  label = "B: Coffee blen"

class C(A):
  label = "C: Tea blen"

class D(B, C):
  pass

cup = D()
print(cup.label) # B: Coffee blen
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)