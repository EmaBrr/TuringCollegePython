from item import Item
from phone import Phone
# from keyboard import Keyboard # doesn't work

item1 = Item('MyItem', 750)
# item1.name = 'OtherItem'
#  As we can see we can easily rewrite the name, so we wrote function in Item.py that it would read only

# print(item1.read_only_name)

# item1.read_only_name = 'aaaasdd'

# with this @name.setter we will be able to change

# item1.name = 'aaaaaaaaaaaaa' #name is too long
print(item1.name)

# Incapsulation:

print(item1.price)
print(item1.apply_increment(0.2))

# Abstraction

item1 = Item('MyItem', 750, 6)

item1.send_email()

item1 = Keyboard('MyItem', 750)