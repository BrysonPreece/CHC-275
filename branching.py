x = 10
if x % 2 ==0:
    print (f"{x} is divisible by 2")
    print ("Test")
else:
    print ("This is not part of the if statement")

x = 10
if x % 2 ==1:
    print (f"{x} is divisible by 2")
    print ("Test")
else:
    print ("This is not part of the if statement")

x = 10
if x % 5 ==0:
    print (f"{x} is divisible by 5")
elif x % 2 ==0:
    print (f"{x} is divisible by 2")
else:
    print (f"{x} is not divisible by 5 or 2")
    