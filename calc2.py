print ("Welcome to the calculator")
print ("1. addition")
print ("2. subtraction")
print ("3. multiplication")
print ("4. division")
option = input ("Enter your option:")

if option == "addition":
    x = input ("What is num 1?")
    y = input ("What is num 2?")
    x = int(x)
    y = int(y)
    z = x + y
    z = int(z)
    print (f"The sum of {x} and {y} is {z}")
elif option =="subtraction":
    x = input("What is num 1?")
    y = input ("What is num 2?")
    x = int(x)
    y = int(y)
    z = x - y
    z = int(z)
    print (f"The difference of {x} and {y} is {z}")

elif option == "multiplication":
    x = input("What is num 1?")
    y = input ("What is num 2?")
    x = int(x)
    y = int(y)
    z = x * y
    print (f"The product of {x} and {y} is {z}")
   
elif option == "division":
    x = input("What is num 1?")
    y = input ("What is num 2?")
    x = int(x)
    y = int(y)
    z = x / y
    print (f"The quotient of {x} and {y} is {z}")
    


