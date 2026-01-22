def makelist():
    check = False
    nums = []
    while check == False:
        option = input("Enter numbers please: ").strip().lower()
        if option == "stop":
            check = True
        else:
            nums.append(option)
    return nums
list1 = makelist()
print(list1)
list2 = makelist()
print(list2)
