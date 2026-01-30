def getMedian(userList):
    length = len(userList)
    middle = length // 2
    if length % 2 == 1:
        middle = int(length/2)
        return (userList[middle])
    else:
        mid1 = int(length / 2) - 1
        mid2 = int(length / 2)
        return (userList[mid1] + userList[mid2]) / 2
oddlist = [2,4,6,8.10]
oddMedian = getMedian(oddlist)
print("Median of odd list: ", oddMedian)

evenlist = [1,3,5,7]
evenMedian = getMedian(evenlist)
print("Median of even list:", evenMedian)

oddlist2 = [4,68,102,56,66,48,1008]
oddMedian = getMedian(oddlist2)
print("Median of odd list2:", oddMedian)

evenlist2 = [67,69,841,83,9]
evenMedian = getMedian(evenlist2)
print("Median of even list2: ", evenMedian)

print("Congrats!!! You Found all the Medians!!!")