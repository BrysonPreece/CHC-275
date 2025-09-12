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
    
x = 10
if x > 5 and x > 15:
    print (f"{x} is greater than 5 and 15")
    
if x > 5 or x > 15:
    print (f"{x} is greater than 5 or 15")
    
    
    
year = input ("Enter your year:")
if year == "freshman":
    print ("Your grade level is 9")
elif year =="sophomore":
    print ("Your grade level is 10")
elif year == "junior":
    print ("Your grade level is 11")
elif year == "senior":
    print ("Your grade level is 12")
    
