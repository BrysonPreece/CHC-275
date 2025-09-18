print ("Pick two numbers.")
x = input ("What is num 1?")
y = input ("What is num 2?")
x = int(x)
y = int(y)
if x > y:
    print (f"{x} is greater than {y}. Number one wins!")
elif x < y:
    print (f"{x} is less than {y}. Number two wins!")
elif x == y:
    print (f"{x} is equal to {y}. It's a tie!")