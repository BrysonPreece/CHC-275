def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power (x,y):
    return x ** y
def main():
    print("Welcome to the calculator.")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. Power")
    check = False
    while check == False:
        option = input("Enter your option 1. addition 2. subtraction 3. multiplication 4. division. Type quit to exit: ").strip().lower().split()
        option = "".join(option)
        if option == "1":
            try:
                x = input ("Enter number 1:")
                y = input ("Enter number 2:")
                x = int(x)
                y = int(y)
                add = x + y
                print(add)
            except ValueError:
                print("x and y must be numbers!!!")
            finally:
                print("Thanks for using the calculator")
        elif option == "2":
            try:
                x = input ("Enter number 1:")
                y = input ("Enter number 2:")
                x = int(x)
                y = int(y)
                subtract = x - y
                print(subtract)
            except ValueError:
                print("x and y must be numbers!!!")
            finally:
                print("Thanks for using the calculator")
        elif option == "3":
            try:
                x = input ("Enter number 1:")
                y = input ("Enter number 2:")
                x = int(x)
                y = int(y)
                multiply = x * y
                print(multiply)
            except ValueError:
                print("x and y must be numbers!!!")
            finally:
                print("Thanks for using the calculator")
        elif option == "4":
            try:
                x = input ("Enter number 1:")
                y = input ("Enter number 2:")
                x = int(x)
                y = int(y)
                divide = x / y
                print(divide)
            except ValueError:
                print("x and y must be numbers!!!")
            finally:
                print("Thanks for using the calculator")
        elif option == "5":
            try:
                x = input ("Enter number 1:")
                y = input ("Enter number 2:")
                x = int(x)
                y = int(y)
                power = x**y
                print(power)
            except ValueError:
                print("x and y must be numbers!!!")
            finally:
                print("Thanks for using the calculator")

        elif option == "quit":
            print("Goodbye")
            check = True
        else:
            print("Not an option you can do")
if __name__ == "__main__":
    main()