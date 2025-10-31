print("Welcome to the Escape Room!!!")
print("You are traveling in a train traveling to go see your grandparents for Christmas. Suddenly, you get knocked out unexpectedly by a hard object.")
print("You then fall onto the floor unconscious and you can't remember anything.")
print("You wake up tied up in a chair in the caboose of the train. You need to get to the front of the train to stop the train and escape.")
print("**************************************************************************************************")

check = False
while check == False:
    option = input("You look around the room. You see a knife on the floor. Press P to pick up the knife. ").strip().lower()
    if option == "p":
        print("**************************************************************************************************")
        print("You picked up the knife to cut the rope. You are now free to move around the room.")
        print("You look around the room. There is a door with a keyhole. You need a key to escape the Caboose.")
        print("There is a painting on the wall, a shelf that is too high to reach, a beanbag, and a safe with a combination to unlock. What do you do? ")
        check = True
    else:
        print("That is not an option that you can do.")

check = False
while check == False:
    option = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION ").strip().lower()
    print("**************************************************************************************************")
    if option == "1" or option == "1.":
        print("**************************************************************************************************")
        print("You investigate the safe. A combination is needed to unlock it.")
        print("**************************************************************************************************")
    elif option == "2" or option == "2.":
        print("**************************************************************************************************")
        print("You investigate the shelf. It looks like something is up there that can be useful. But you can't reach it because you are only 4'1 and not 6'7.")
        print("**************************************************************************************************")
    elif option == "3" or option == "3.":
        print("**************************************************************************************************")
        print("You investigate the beanbag. It looks like you found a hammer. That can be useful for breaking things.")
        print("You can use the hammer by typing the word HAMMER.")
        print("**************************************************************************************************")
        tool = input("Type HAMMER to use it now, or press Enter to go back: ").strip().lower().split()
        tool = "".join(tool)
        if tool == "hammer":
            option = input("Where would you like to use the hammer? 1. Painting, 2. Shelf, 3. Beanbag, 4. Door, 5. Safe. TYPE THE NUMBER THAT CORRESPONDS WITH THE ACTION ").strip().lower()
            print("**************************************************************************************************")
            check = False
            while check == False:
                if option == "1" or option == "1.":
                    print("You use the hammer on the painting. It breaks apart and reveals a huge hole on the other side.")
                    print("You step in the hole and find a ladder.")
                    print("You look on the wall and see words that say: THERE IS NO ESCAPE!!!")
                elif option == "2"or "2."or "3"or "3."or "4"or "4."or "5"or "5.":
                    print("You tried to use the Hammer, but it failed.")
                    check = True
                else:
                    print("That is not an option that you can do.")
                    check = True
    elif option == "4" or option == "4.":
        print("**************************************************************************************************")
        print("There is a painting on the wall. It gives you a chill. It looks like it can be broken with something.")
        print("**************************************************************************************************")
    else:
        print("That is not an option that you can do.")