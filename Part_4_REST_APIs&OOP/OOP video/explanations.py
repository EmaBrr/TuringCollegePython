# This is an example of multiple variables before starting to understand why we need objects

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))

# <class 'str'>
# <class 'int'>
# <class 'int'>
# <class 'int'>

# Creation of the class:

# First example:
class Item:
    pass

# Second example:
class Item:
    Explanation on "self". When we want to call function, we should call item1 at first, and only then use the arguments for formula
    def calculate_total_price(self, x, y ): # not function - method
        return x * y
    
item1 = Item() 
item1.name = 'Phone' 
item1.price = 100
item1.quantity = 5
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

print(item1.calculate_total_price(item1.price, item1.quantity)) # 500

# Third example:
class Item:
    def __init__(self, name): # with __ is called magic methods
        print('I am created')
    def calculate_total_price(self, x, y ): # not function - method
        return x * y

item1 = Item() # It would return 'I am created'

# Fourth example:
class Item:
    def __init__(self, name, price, quantity=0): # with __ is called magic methods
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self): # not function - method
        return self.price * self.quantity

item1 = Item("Phone", 100, 5) 
item2 = Item('Laptop', 1000, 3)

print(item1.name)
print(item2.name)
# # Phone
# # Laptop
print(item1.price)
print(item2.price)
# # 100
# # 1000
print(item1.quantity)
print(item2.quantity)
# # 5
# # 3

print(item1.calculate_total_price()) #500
print(item2.calculate_total_price()) #3000

# Fifth example (adding data types validation):

class Item:
    pay_rate = 0.8 # Class attribute. The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): # not function - method
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # self.price = self.price * Item.pay_rate


item1 = Item("Phone", 100, 5) 
item2 = Item('Laptop', 1000, 3)

print(item1.name)
print(item2.name)
# # Phone
# # Laptop
print(item1.price)
print(item2.price)
# # 100
# # 1000
print(item1.quantity)
print(item2.quantity)
# # 5
# # 3

print(item1.calculate_total_price()) #500
print(item2.calculate_total_price()) #3000

print(Item.pay_rate) # 0.8
print(item1.pay_rate) # 0.8, if it would not be created specifically for item1 , then it will show the attribute of the class

print(Item.__dict__) 
# # Result:
# # {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x000001B799339080>, 'calculate_total_price': <function Item.calculate_total_price at 0x000001B7993391C0>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}

# print(item1.__dict__) # {'name': 'Phone', 'price': 100, 'quantity': 5}

# item1.apply_discount()
# print(item1.price) # 80.0

# # what should we do if we want to apply 30% discount for item2?
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price) # if in the formula we have this self.price = self.price * Item.pay_rate then it will apply 0.8 anyways. need to change it to self.pay_rate

# Sixth example:

class Item:
    pay_rate = 0.8 # Class attribute. The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self): # not function - method
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Without this def, when we print all we get weird objects, in order to make it prettier we will use this
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"    

item1 = Item("Phone", 100, 5) 
item2 = Item('Laptop', 1000, 3)        
item3 = Item('Cable', 10, 5)  
item4 = Item('Mouse', 50, 5)  
item5 = Item('Keyboard', 75, 5)  

print(Item.all)

# # Before fixing: [<__main__.Item object at 0x000001A4F6817390>, <__main__.Item object at 0x000001A4F5AFE950>, <__main__.Item object at 0x000001A4F6817410>, <__main__.Item object at 0x000001A4F6817490>, <__main__.Item object at 0x000001A4F6817510>]
# # After fixing: [Item('Phone', '100', '5'), Item('Laptop', '1000', '3'), Item('Cable', '10', '5'), Item('Mouse', '50', '5'), Item('Keyboard', '75', '5')]

# for instance in Item.all:
#     print(instance.name)

# # Phone
# Laptop
# Cable
# Mouse
# Keyboard

# Seventh example (with csv file):

import csv

class Item:
    pay_rate = 0.8 # Class attribute. The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls): #Class method
        with open('Module 1. Part 4. OOP video\data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero 5.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"    

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.5))

# {'name': 'Phone', ' price': ' 100', ' quantity': ' 1'}
# {'name': 'Laptop', ' price': ' 1010', ' quantity': ' 3'}
# {'name': 'Cable', ' price': ' 10', ' quantity': ' 5'}
# {'name': 'Mouse', ' price': ' 50', ' quantity': ' 5'}
# {'name': 'Keyboard', ' price': ' 75', ' quantity': ' 5'}

#  Why use staticmethod or classmethod

# @staticmethod is used to define a method that is bound to a class but does not depend on the class or its instance. It's often used for utility functions that don't need access to instance-specific data.

# @classmethod is used to define a method that is bound to a class and takes the class itself as its first argument. It's commonly used to create alternative constructors or manipulate class-specific attributes.

# Eight example (with csv file)

import csv

class Item:
    pay_rate = 0.8 # Class attribute. The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls): #Class method
        with open('Module 1. Part 4. OOP video\data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero 5.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"    

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater or equal to zero!'

        # Assign to self object
        self.broken_phones = broken_phones

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.5))


phone1 = Phone('jscPhonev10', 500, 5, 1)
print(phone1.calculate_total_price())
# phone1.broken_phones = 1
phone2 = Phone('jscPhonev20', 700, 5, 1)
# phone2.broken_phones = 1

print(Item.all)
print(Phone.all)

# Polymorphism example is len because if name is JIM it would say 3, but if we have array with 2 items in it, it will return 2