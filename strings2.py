option = input("Enter a list of names seperated by spaces")
print(option)
names = option.split()
print (names)
bitstream = "How0110101Are0110101You?"
message = bitstream.split("0110101")
print(message)
mystr = "Hello#How#Are#You"
message = mystr.split('#')
print (message)
space = " "
fruits = ["apples", "oragnes", "pears", "mangoes"]
combined = space.join(fruits)
print(combined)
combined = " ".join(fruits) #More successful way
print(combined)
sum = 4 + 5
print(sum)
str1 = "Hello"
str2 = "World"
concat = str1+str2 #NOT COMMUNITIVE
print (concat)
