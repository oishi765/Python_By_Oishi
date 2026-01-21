print("Welcome to Online Shopping Cart")
cart = {}

cart = {}

def add_item():
    name = input("Item: ")
    price = int(input("Price: "))
    qty = int(input("Qty: "))
    cart[name] = cart.get(name, 0) + price * qty

def show_bill():
    total = 0
    for item, price in cart.items():
        print(item, price)
        total += price
    print("Total Bill:", total)

while True:
    print("1.Add 2.Bill 3.Exit")
    c = input()
    if c == "1":
        add_item()
    elif c == "2":
        show_bill()
    else:
        break
