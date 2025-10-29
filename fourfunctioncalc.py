print("Welcome to the calculator.")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
check = False
while check == False:
    option = input("Enter your option 1. addition 2. subtraction 3. multiplication 4. division. PLEASE ENTER THE WORD, NOT THE NUMBER!!!!! Type quit to exit").strip().lower().split()
    option = "".join(option)
    if option == "addition":
        try:
            x = input ("Enter number 1:")
            y = input ("Enter number 2:")
            x = int(x)
            y = int(y)
            Addition = x + y
            print(Addition)
        except ValueError:
            print("x and y must be numbers!!!")
        finally:
            print("Thanks for using the calculator")
    elif option == "subtraction":
        try:
            x = input("Enter number 1:")
            y = input("Enter number 2:")
            x = int(x)
            y = int(y)
            subtraction = x - y
            print(subtraction)
        except ValueError:
            print("x and y must be numbers!!!")
        finally:
            print("Thanks for using the calculator")
    elif option == "multiplication":
        try:
            x = input("Enter number 1:")
            y = input("Enter number 2:")
            x = int(x)
            y = int(y)
            print(x * y)
        except ValueError:
            print("x and y must be numbers!!!")
        finally:
            print("Thanks for using the calculator")
    elif option == "division":
        try:
            x = input("Enter number 1:")
            y = input("Enter number 2:")
            x = int(x)
            y = int(y)
            print(x / y)
        except ValueError:
            print("x and y must be numbers!!! What are you doing!!!!!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        finally:
            print("Thanks for using the calculator")
    elif option == "quit":
        print("Goodbye!")
        check = True
    else:
        print("Invalid option. Please enter addition, subtraction, multiplication, division or quit.")