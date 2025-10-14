money = input("Enter your value:")
money = int(money)
#We 'parse' our input
mystr = "hello"
for char in mystr:
    print(char) #Prints every individual character in HELLO

print ("for - i loop")
for i in range(len(mystr)):
    print (mystr[i])

print ("1. Add an account")
print ("2. Delete an account")
print ("3. Print all accounts ")
print ("4.  Withdraw money from a chosen account")
print ("5. Deposit money into an account")
print ("6. Transfer money between two accounts")
print ("7. Exit.")

option = input ("Select your option").strip().lower()
if option == "deposit":
    print("Deposit sequance")
    
elif option == "Add an account":
    print(" Select a name to add an account")
    
elif option == "Delete an account":
    print(" Select a name to remove an account")
    
elif option == "Exit":
    print("Goodbye :)")
    
    
mystr = "Hello"
print (mystr)
mystr = mystr.strip().lower() #Or .upper()
print (mystr)

money = "10"
if money.isnumeric():
    money = int(money)
    val = money + 5 
    print(val)
else:
    print ("That is not a number")
    