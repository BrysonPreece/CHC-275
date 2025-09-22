check = False
option = input ("Enter a number.")
option = int(option)
while check == False:
        if option % 2 ==1:
                option = option * 3 + 1
                print (option)
        elif option % 2 ==0:
                option = option / 2
                print (option)
        if option == 1:
                check = True