def getMin(list):
    smallest = list[0]
    i = 0
    while i < len(list):
        if list[i] < smallest:
            smallest = list[i]
        i = i + 1
    return smallest