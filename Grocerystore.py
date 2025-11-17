file = open ("Glist.txt", "r")
bufferGlist = file.readlines()
print(bufferGlist)
file.close()
Glist = []
print ("Welcome to the grocery store")
print("1. Add to your cart")
print("2. Remove items")
print("3. Check out")
check = False
while check == False:
    option = input("What would you like to do today? Please enter the number without any periods")
    if option == "1":
        check = True
check = False
while check == False:
    print("What items would you like to add to your cart?")
    option = input("Bananas,1.75. Apples,1.50. Raw steak,4.75. Milk,2.50. Orange Juice,3.50. Eggs,10.99. Rotisserie Chicken,6.50. Rice,4.00. Loaf Of Bread,2.00.")
    if option == "Bananas":
        Glist.append("Bananas")
    print("You added Bananas to your Glist")
    print(Glist)
    elif option == "Apples":
    Glist.append("Apples")
    print("You added Bananas to your Glist")
    