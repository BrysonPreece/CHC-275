total = 0.0
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
    option = input("Bananas,1.75. Apples,1.50. Raw steak,4.75. Milk,2.50. Orange Juice,3.50. Eggs,10.99. Rotisserie Chicken,6.50. Rice,4.00. Loaf Of Bread,2.00. Type quit to exit").strip().lower().split()
    option = "".join(option)
    if option == "Bananas":
        Glist.append("Bananas")
        print("You added Bananas to your Glist")
        print(Glist)
    elif option == "Apples":
        Glist.append("Apples")
        print("You added Bananas to your Glist")
        print(Glist)
    elif option == "Raw Steak":
        Glist.append("Raw Steak")
        print("You added Raw Steak to you Glist")
        print(Glist)
    elif option == "Milk":
        Glist.append("Milk")
        print("You added Milk to your Glist")
        print(Glist)
    elif option == "Orange Juice":
        Glist.append("Orange Juice")
        print("You added Orange Juice to your Glist")
        print(Glist)
    elif option == "Rotisserie Chicken":
        Glist.append("Rotisseri Chicken")
        print("You added Rotisseri Chicken to your Glist")
        print(Glist)
    elif option == "Rice":
        Glist.append("Rice")
        print("You added Rice to your Glist")
        print(Glist)
    elif option == "Loaf of bread":
        Glist.append("Loaf of bread")
        print("You added Loaf of Bread to your Glist")
        print(Glist)
    elif option == "Quit":
        print("Ok :)")
    check = True
else:
    print("That is not an option you can do")