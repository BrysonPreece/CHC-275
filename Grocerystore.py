print("Welcome to the supermarket")
check = False
total = 0.0
file = open("Glist.txt", "r")
buffer = file.readlines()
print(buffer)
file.close()
Glist = []
for i in range(len(buffer)):
    Glist.append(buffer[i].strip().split(","))
items = []
prices = []

for i in range(len(Glist)):
    items.append(Glist[i][0])
    prices.append(Glist[i][1])
    
    
cart = []
cart = 0.0

while check == False:
    print("*******************************************************************************")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. Check out")
    choice = int(input("Enter your option (1, 2, 3): "))
    print("*******************************************************************************")
    if choice == 1:
        check2 = False
        while check2 == False:
            print("*******************************************************************************")
            print("All available and their prices")
        for i in range(len(all)):
            print(f"{i+1} {items{i}}: {prices{i}}")
        try: item = input("\nEnter the index of the item you want to add: ")
        index = int(item) - 1
        quantity = input("Enter the quantity you want to add: ")
        quantity = int (quantity)
        print(f"Added {quantity} of {items[index]} to your cart.\n")
        itemscost = float(prices[index]) * quantity
        cost += itemscost
        cart.append((items[index], quantity, float(prices[index])))
        except Exception as e:
            print (f"An error has risen. Too bad :(")
        choice2 = input("Would you like to add another item to ur cart? Y or N")
        print("*******************************************************************************")
        if choice2 == "Y":
            print("")
        elif choice2 == "N":
            check2 = True
        else:
            print("Invalid. System error.")
    elif choice == "2":
        print("*******************************************************************************")
        if len(cart) ==0:
            print("Your cart is empty :(\n")
        else:
            print("Items that are in your cart")
            for i, (itemname, qty, price) in enumerate(cart):
                print(f"{i+1}. {itemname} x{qty} at ${price} each = ${qty * price:2f}")
            print()
            try:
                item = input("Enter the index of the item you want to remove: ")
                index = int(item) - 1
                if 0 <= index < len(cart):
                    quantity = input("Enter the quantity you want to remove")
                    quantity = int(quantity)
                    itemname, currentQty, price = cart[index]
                    if quantity >= currentQty:
                        removedCost = currentQty * price
                        cost -= removedCost
                        print(f"Removed all {currentQty} of {item_name} from your cart.\n")
                        cart.pop(index)
                    else:
                        removedCost = quantity * price
                        cost -= removedCost
                        cart[index] = (item_name, currentQty - quantity, price)
                        print(f"Removed {quantity} of {item_name} from your cart.\n")
                        print("*******************************************************************************")
                    if len(cart) == 0:
                        print("Your cart is now empty.\n")
                    else:
                        print("Updated cart contents:")
                        for i, (item_name, qty, price) in enumerate(cart):
                            print(f"{i+1}. {item_name} x{qty} at ${price} each = ${qty * price:.2f}")
                        print()
                else:
                    print("Invalid index!\n")