mylist = [5,10,15,20,25]
print (mylist)
print (mylist[0])
print (mylist [0] * mylist [1])
sum = mylist[0]+ mylist[3]
print (sum)
print (mylist[-1])
mylist2 = [1,10,True,"Hello"]
print (mylist2)
i = 0
print ("Individuel Elements")
while i <=3:
    print (mylist[i])
    i = i + 1
print ("printing size")
print (len(mylist))
mylist = [5,10,15,20,25, 30, 35]
i = 0
while i <= len (mylist) - 1:
    print (mylist[i])
    i = i + 1
    print ("for loop example")
for num in mylist:
    print (num)
    
print (mylist)
i = 0 
while i <= len (mylist) - 1:
    mylist[i] = mylist[i] + 5
    i = i + 1
print (mylist)
