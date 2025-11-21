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
        try: