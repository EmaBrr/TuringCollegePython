menu = {
    'pizza': 10, 
    'sandwich': 8,
    'pasta': 11,
    'tea': 2, 
    'coffee': 3
}

for items, price in menu.items():
    print(price)

def restaurant():
    menu_items = []
    prices = []
    global total_price 
    total_price = 0
    for item, price in menu.items():
        menu_items.append(item)
        prices.append(price)
    
    def inner_function():
        order = input('Enter your order:')
        global total_price 
        if order.lower() in menu_items:
            print(f'Price for your order is: {menu[order.lower()]} eur')
            total_price += menu[order.lower()]
            print(f'Total price for your order is: {total_price} eur')
            inner_function()
        elif order.lower() == '':
            print(f'Total price for your order is: {total_price} eur')
        else:
            print('We do not have this on our menu.')
            inner_function()

    inner_function()
    
restaurant()
