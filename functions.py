def foo(): # def- <function name>(): is called the function header
            #includes the function defination, the function name, and the parameter list
    print("bar")
foo() #Always need to end with parentheses. Tab back over to left

def add5(num):
    #function name = add5
    #parameter list = num
    #num is a placeholder
    num = num + 5
    print(num)
add5(8)
add5(4)
mynum = 10
add5(mynum)

def multiply (num1, num2):
    #function name = multiply
    #parameter list = num1 and num2
    
    product = num1*num2
    print(product)
multiply(3,5)
multiply(4,10)
multiply(4,"a")

def add(num1, num2):
    sum = num1+num2
    print(sum)
add(2,5)
add("Hello","World")
add("World", "Hello")

def studentUpdate(name,age,gpa):
    print(f"Student Name: {name}, Student Age: {age}, Student gpa: {gpa}")
studentUpdate("bob", 15,4.0)

def update(num1):
    num1 = num1 + 10
x = 5
update(x)
print(x)

#Imnmutable = its state can't be changed
#Mutable = its state can be changed
#Intergers are immutable
#Mutable stuff = Lists and strings
mylist = [1,2,3,4]
def update2(nums):
    nums.append(5)
update2(mylist)
print(mylist)

def updateBalance(money,change):
    money = money - change
    return money #All return does is tell the computer to remember something
balance = 500
balance = updateBalance(balance, 200)
print(balance)