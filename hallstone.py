check = False
option = input ("Enter a number.")
option = int(option)
while check == False:
        if option % 2 ==1:
                option = input (f"{option * 3 + 1}")
                print (option)
        elif option % 2 ==0:
                option = input (f"{option / 2}")
                print (option)
                check = True