""" import recipes.flavors

print(recipes.flavors.make_capuccino()) """

from recipes.flavors import make_capuccino, make_latte

print(make_capuccino())
print(make_latte())

from .utils.discounts import get_discount # not needed if we are in the same directory

print(get_discount("regular"))