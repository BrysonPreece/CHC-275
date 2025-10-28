try:
    x = input("Enter number 1:")
    y = input("Enter number 2:")
    x = int(x)
    y = int(y)
    quotient = x/y
    print (quotient)
    #Dividing by 0 is no goood
except ValueError and ZeroDivisionError:
    print ("x and y must be numbers and can't be Zero")
    
    
try:
    x = input("Enter number 1:")
    y = input("Enter number 2:")
    x = int(x)
    y = int(y)
    quotient = x/y
    print (quotient)
    #Dividing by 0 is no goood
except ValueError and ZeroDivisionError:
    print ("x and y must be numbers and can't be Zero")
except TypeError:
    print("Variables must be intergers ")
except Exception as e:
    print(e)
finally:
    print("Thanks for using the calculator")
#Try: attempts to executes the code blocks, if an exception is thrown, jump to excpet block
#Except: if try fails, throws an exception, the except is matched to the corresponding except keyboard and executes that code block
# Fianlly: After all tries and excpets are made, codeblocks after finally are executed no matter what