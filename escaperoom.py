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
        print("**************************************************************************************************")

        check = True
    else:
        print("That is not an option that you can do.")

check = False
while check == False:
    option = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. 5. Investigate the door.").strip().lower()
    print("TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION. DO NOT INCLUDE A PERIOD")
    print("**************************************************************************************************")
    if option == "1":
        print("**************************************************************************************************")
        print("You investigate the safe. A combination is needed to unlock it.")
        print("**************************************************************************************************")
    elif option == "2":
        print("**************************************************************************************************")
        print("You investigate the shelf. It looks like something is up there that can be useful. But you can't reach it because you are only 4'1 and not 6'7.")
        print("**************************************************************************************************")
    elif option == "3":
        print("**************************************************************************************************")
        print("You investigate the beanbag. It looks like you found a hammer. That can be useful for breaking things.")
        print("You can use the hammer by typing the word HAMMER.")
        print("**************************************************************************************************")
        check = True
    elif option == "4":
        print("You Investigate the painting. It shows a picture of an old man.")
        print ("It reminds you of the book The Old Man and The Sea that you read in high school in your freshman year.")
    elif option == "5":
        print ("You investigate the door. It is a metal door that can't be broken.")
        print("You try pulling and pushing the door, but it won't budge.")
        print("You think about hitting the gym more.")
        print("**************************************************************************************************")
    else:
        print("That is not an option that you can do")
check = False
while check == False:
    tool = input("Type HAMMER to use it now: ").strip().lower().split()
    tool = "".join(tool)
    print("**************************************************************************************************")
    if tool == "hammer" or tool == "hammer.":
        check = True
    else:
        print("That is not an option you can do")
        print("**************************************************************************************************")


check = False
while check == False:
    option = input("Where would you like to use the hammer? 1. Painting, 2. Shelf, 3. Beanbag, 4. Door, 5. Safe. TYPE THE NUMBER THAT CORRESPONDS WITH THE ACTION. DO NOT INCLUDE A PERIOD.").strip().lower().split()
    option = "".join(option)
    if option == "1":
            print("You use the hammer on the painting. It breaks apart and reveals a huge hole on the other side.")
            print("You step in the hole and find a ladder and a pouch that can be used for invitory.")
            print("You look on the wall and see words that say: THERE IS NO ESCAPE!!!")
            print("**************************************************************************************************")
            check = True

    elif option == "2":
            print("You try and use your hammer on the shelf but it's too high up to use.")
            print("**************************************************************************************************")

    elif option == "3":
            print("You already searched the beanbag enough. It's usless now.")
            print("**************************************************************************************************")

    elif option == "4":
            print("The door is made with a hard steel.")
            print("You try and use the hammer on the door, but it's not very effective. It didn't make a dent in it.")
            print("You feel stupid because you have been playing Pokemon for 67 years now.")
            print("You should have known that steel is not very effective onto steel types or objects.")
            print("**************************************************************************************************")

    elif option == "5":
            print("You try and use the hammer on the safe. It does nothing to it.")
            print("**************************************************************************************************")
    else:
        print("The action you wish to do does not compute with our system.")
        print("Please try again later.")
        print("**************************************************************************************************")
Invitory = ["Ladder"]

check = False
while check == False:
        print("You add the Ladder to your invitory. What do you do now?")
        print("1. Check the painting. 2. Check the Shelf. 3. Check the beanbag. 4. Check the Door. 5. Check the Safe. 6. Open Invintory")
        option = input("Enter the number that corresponds to the action. Remember, don't type periods.")
        print("**************************************************************************************************")

        if option == "1":
            print("You already inspected the painting. There is nothing to do here besides looking at that message on the wall.")
            print("The message says: THERE IS NO ESCAPE!!!")
            print("**************************************************************************************************")

        elif option == "2":
            print("The shelf is too high up to reach. You can reach whatever is up there with an object.")
        check = False
        while check == False:
            option = input("Would you like to use an item from your invintory? Type Yes or No").strip().lower().split()
            option == "".join(option)
            print("**************************************************************************************************")
            if option == "Yes":
                print(Invitory)
                option = input("Please choose an item from your invintory to use.")
            if option == "ladder":
                print("You used the ladder to climb up the shelf. You see something and add it to your invintory")
                print("You added a code to the invontory")
                print("**************************************************************************************************")
                check = True
            elif option == "No":
                print("Ok")
                    
            elif option == "3":
                print("The beanbag has already been inspected.")
                print("**************************************************************************************************")

            elif option == "4":
                print("The door is made of steel. It won't budge without a key.")
                print("**************************************************************************************************")

            elif option == "5":
                print("The safe is locked. You need a code to open it.")
                print("**************************************************************************************************")

            elif option == "6":
                print (Invitory)
                print("**************************************************************************************************")
            else:
                print("That is not an object that you can use in your invintory")