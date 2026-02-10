""" 
Name: Bryson
Section: 1
Description: Lab 4 
"""
from math import sqrt


"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    nums = []
    check = False
    while check == False:
        try:
            print("Type the word stop to stop the code.")
            option1 = input("Please enter a number: ").lower().strip()
            if option1 == "stop":
                check = True
            else:
                option1 = int(option1)
                nums.append(option1)
        except Exception as e:
            print(e)
    return nums

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("\n*************************************************")
    print("Welcome to the Calc!")
    print("1. Mean list")
    print("2. Median list")
    print("3. Minimum list")
    print("4. Maximum list")
    print("5. Standard Dev list")
    print("6. Quit")
    input1 = input("Please enter your selection: ")
    print("*************************************************")
    return input1
"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    if not userList:
        raise ValueError("Cannot compute mean of an empty list. System error :(")
    return sum(userList) / len(userList)

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)
    if not userList:
        raise ValueError ("Cannot compute median of an empty list.")
    n = len(userList)
    m = n // 2
    return userList [m] if n % 2 else (userList[m-1]+ userList[m]) / 2

""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    if not userList:
        return None
    candidate = userList[0]
    i = 1
    while i < len(userList):
        if userList[i] < candidate:
            candidate = userList[i]
        i+=1
    return candidate
    

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    print("63 lines left")
""" 
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    pass



def main():
    pass


if __name__ == "__main__":
    main()