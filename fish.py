print ("You need to figure out what kind of fish they have. Either carnivorous, salt water, or community. Type what you think what kind of fish they have.")
option = input ("What fish do you have?:")
if option == "carnivorous":
    print ("Type Yes or No.")
    option = input ("Do you already have it?")
elif option == "salt water":
    print ("You are a fancy fish parent.")
if option == "Yes":
    print ("Too bad so sad. Womp Womp. :(")
elif option == "No":
    print ("Enjoy!")
elif option == "community":
    print ("You should get more than one.")
else:
    print ("I don't think that is a type of fish.")
