print("\nWelcome to the Sage Grocery Store!")
check = False
file = open("Glist.txt", "r")
buffer = file.readlines()
file.close
all=[]
for i in range(len(buffer)):
    all.append(buffer[i].strip().split(","))
items = []
prices = []
for i in range(len(all)):
    items.append(all[i][0])
    prices.append(all[i][1])

cart = []
cost = 0.0

while check == False:
    print("***********************************************************************************************")
    print("1. Add an item to cart")
    print("2. Remove an item from cart")
    print("3. Check Out")
    choice = input("Enter your selection (1, 2, 3): ")
    print("***********************************************************************************************")
    if choice == '1':
        check2 = False
        while check2 == False:
            print("***********************************************************************************************")
            print("All available items and their prices:")
            for i in range(len(all)):
                print(f"{i+1}. {items[i]}: ${prices[i]}")
            try:
                item = input("\nEnter the index of the item you want to add: ")
                index = int(item) - 1
                quantity = input("Enter the quantity you want to add: ")
                quantity = int(quantity)
                print(f"Added {quantity} of {items[index]} to your cart.\n")
                itemsCost = float(prices[index]) * quantity
                cost += itemsCost
                cart.append((items[index], quantity, float(prices[index])))
            except Exception as e:
                print(f"An unforseen error has occurred: {e}")
            choice2 = input("Would you like to add another item? (y/n) ")
            print("***********************************************************************************************")
            if choice2 == 'y':
                print("")
            elif choice2 == 'n':
                check2 = True
            else:
                print("Invalid input, please try again")
    elif choice == '2':
        print("***********************************************************************************************")
        if len(cart) == 0:
            print("Your cart is empty!\n")
        else:
            print("Items in your cart:")
            for i, (itemName, qty, price) in enumerate(cart):
                print(f"{i+1}. {itemName} x{qty} at ${price} each = ${qty * price:.2f}")
            print()
            try:
                item = input("Enter the index of the item you want to remove: ")
                index = int(item) - 1
                if 0 <= index < len(cart):
                    quantity = input("Enter the quantity you want to remove: ")
                    quantity = int(quantity)
                    itemName, currentQty, price = cart[index]
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
                        print("***********************************************************************************************")
                    if len(cart) == 0:
                        print("Your cart is now empty.\n")
                    else:
                        print("Updated cart contents:")
                        for i, (item_name, qty, price) in enumerate(cart):
                            print(f"{i+1}. {item_name} x{qty} at ${price} each = ${qty * price:.2f}")
                        print()
                else:
                    print("Invalid index!\n")
            except Exception as e:
                print(f"An unforseen error has occurred: {e}")
    elif choice == '3':
        tax = cost * 0.06
        total = cost + tax
        print("***********************************************************************************************")
        print(f"Your total is: ${total:.2f} (including ${tax:.2f} sales tax)")
        print("Thank you for shopping at Sage Grocery Store!")
        print("***********************************************************************************************")
        check = True
    else:
        print("Invalid input. Unfortunately they took away my self destrcut sequence.")