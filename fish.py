print ("You need to figure out what kind of fish they have. Either carnivorous, salt water, or community. Type what you think what kind of fish they have.")
option = input ("What fish do you have?:")
if option == "carnivorous":
    print ("Type Yes or No.")
    fish = input ("Do you already have it?")
if fish == "Yes":
    print ("Too bad so sad. Womp Womp. :(")
elif fish == "No":
    print ("Enjoy!")