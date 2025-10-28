print ("Welcome to the calculator.")
print ("1. addition")
print ("2. subtraction")
print ("3. multiplication")
print ("4. division")
check = False
while check == False:
    option = input ("Enter your option 1. addition 2. subtraction 3. multiplication 4. division. PLEASE ENTER THE WORD, NOT THE NUMBER!!!!! Type quit to exit")
    if option == "addition":
        try:
            x = input ("What is num 1?")
            y = input ("What is num 2?")
            x = int(x)
            y = int(y)
            Addition = x + y
            print (Addition)
        except ValueError:
            print ("x and y must be numbers!!!")
    