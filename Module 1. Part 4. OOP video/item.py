import csv

class Item:
    pay_rate = 0.8 # Class attribute. The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): # since we put default value as int, we don't need to say again that this shoult be int
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def price(self):
        return self.__price
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        # print('You are trying to get name')
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long!')
        # print('You are trying to set name')
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        return self.__price

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
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"    
    
    def __connect(self, smpt_server): #Private method
        pass #in order to send email we need to connect to server, but it's just for info

    def __prepare_body(self): #Private method
        return f'''
        Hello all, 
        We have {self.name} {self.quantity} times.
        Regards, Ema
        '''
    
    def __send(self): #Private method
        pass

    def send_email(self): # we would be able to run only this since it's not private
        self.__connect()
        self.__prepare_body()
        self.__send()
