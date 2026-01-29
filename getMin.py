def getMin(userlist):
    min = userlist[0]
    i = 0
    while i < len(userlist):
        if userlist[i] < min:
            min = userlist[i]
        i = i + 1
    return min

first = [1,2,3,4]
print(first)
print(f"Minimum of the first list {getMin(first)}")

second = [4,2,1,3]
print(second)
print(f"Minimum of the second list {getMin(second)}")

third = [67,69,41,72,94]
print(third)
print(f"Minimum of the third list {getMin(third)}")

print("You found the minimum. Great Job!!!")