SSE = 0
SSE = SSE + (current-mean)^2
""" 
Name: Bryson
Section: 1
Description: Lab 4 
"""

check = False
while check == False:
    print("1. getlist")
    print("2. printmenu")
    print("getmean")
    print("getmedian")
    print("getmin")
    print("getmax")
    print("getStdDev")
    option = input("What do you want to do? Type in the number. Type q to exit").strip().lower()

"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    pass

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    pass

"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    pass

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)

""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    pass

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    pass

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