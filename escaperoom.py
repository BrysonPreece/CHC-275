print("Welcome to the Escape Room!!!")
print("You are traveling in a train traveling to go see your grandparents for Christmas. Suddenly, you get knocked out unexpectedly by a hard object.")
print("You then fall onto the floor unconscious and you can't remember anything.")
print("You wake up tied up in a chair in the caboose of the train. You need to get to the front of the train to stop the train and escape.")
print("**************************************************************************************************")

check = False
while check == False:
    option = input("You look around the room. You see a knife on the floor. Press P to pick up the knife. : ").strip().lower()
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
    option = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. 5. Investigate the door. : ").strip().lower()
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
        print("**************************************************************************************************")

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
    option = input("Where would you like to use the hammer? 1. Painting, 2. Shelf, 3. Beanbag, 4. Door, 5. Safe. TYPE THE NUMBER THAT CORRESPONDS WITH THE ACTION. DO NOT INCLUDE A PERIOD. : ").strip().lower().split()
    option = "".join(option)
    if option == "1":
            print("You use the hammer on the painting. It breaks apart and reveals a huge hole on the other side.")
            print("You step in the hole and find a ladder and a pouch that can be used for inventory.")
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
Inventory = ["Ladder"]

check = False
while check == False:
        print("You add the Ladder to your inventory. What do you do now?")
        print("1. Check the painting. 2. Check the Shelf. 3. Check the beanbag. 4. Check the Door. 5. Check the Safe. 6. Open Inventory")
        option = input("Enter the number that corresponds to the action. Remember, don't type periods. : ")
        print("**************************************************************************************************")

        if option == "1":
            print("You already inspected the painting. There is nothing to do here besides looking at that message on the wall.")
            print("The message says: THERE IS NO ESCAPE!!!")
            print("**************************************************************************************************")

        elif option == "2":
            print("The shelf is too high up to reach. You can reach whatever is up there with an object.")
            check = True
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
            print (Inventory)
            print("**************************************************************************************************")
        else:
            print("That is not an object that you can use in your inventory")
            print("**************************************************************************************************")
check = False
while check == False:
        option = input("Would you like to use an object from your inventory to climb up the shelf? (Y or N?) : ")
        print("**************************************************************************************************")

        if option == "Y":
            print("ok")
            print("**************************************************************************************************")
            check = True
        elif option == "N":
            print("Too bad")
            print("**************************************************************************************************")


check = False
while check == False:
    print(Inventory)
    option = input ("What object in your inventory would you like to use to climb up the shelf? : ").strip().lower().split()
    option = "".join(option)

    if option == "ladder":
        print("You used the ladder to climb up the shelf. It looks like there is something shiny on the shelf.")
        print("You picked up a code on the shelf")
        print("You added code to your inventory and removed Ladder from your inventory")
        Inventory.append("Code")
        Inventory.remove("Ladder")
        print(Inventory)
        print("**************************************************************************************************")
        check = True

    else:
        print("Action does not compute with our system")
        print("**************************************************************************************************")

check = False
while check == False:
    print("You have now inserted the code into your inventory.")
    print("You feel like you are almost out of here")
    print("TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION. DO NOT INCLUDE A PERIOD")
    print("**************************************************************************************************")
    option = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. 5. Investigate the door. : ").strip().lower()
    print("**************************************************************************************************")
    if option == "1":
        print("**************************************************************************************************")
        print("You investigate the safe. A combination is needed to unlock it.")
        print("**************************************************************************************************")
        check = True
    elif option == "2":
        print("**************************************************************************************************")
        print("You already investigated the shelf already.")
        print("**************************************************************************************************")
    elif option == "3":
        print("**************************************************************************************************")
        print("You already investigated the beanbag.")
        print("**************************************************************************************************")
    elif option == "4":
        print("You already investigated the painting already.")
        print("**************************************************************************************************")

    elif option == "5":
        print ("You investigate the door. It is a metal door that can't be broken.")
        print("You try pulling and pushing the door, but it won't budge.")
        print("You think about hitting the gym more.")
        print("**************************************************************************************************")
    else:
        print("That is not an option that you can do")

check = False
while check == False:
    print("**************************************************************************************************")
    print("It seems the code has some writing on it")
    print("It says the following: ")
    print("**************************************************************************************************")
    print("H3llo. I'm writing to you about this mysterious man on the train. This man is very dangerous ... 2 dangerous")
    print("If you are reading this c0de, you should escape as soon as possible. There is not much time left.")
    print("U6e this code on the safe to unlock it. I believe in you.")
    print("The code is seven digits long, luckly this message incluides some hints, if you can find them ...")
    print("7ust enter the seven digits into the safe, and that should unlock it.")
    print("You got this!1!")
    print("I b5lieve in you")
    print("From - Dr. M")
    print("**************************************************************************************************")
    print("Please enter the seven digits into the safe. Look at the code for clues")
    print("**************************************************************************************************")
    check = True
check = False
while check == False:
    a = input ("Enter number 1 : ")
    if a == "3":
        print("Correct")
        check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    b = input ("Enter number 2 : ")
    if b == "2":
         print ("Correct")
         check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    c = input ("Enter number 3 : ")
    if c == "0":
         print("Correct")
         check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    d = input ("Enter number 4 : ")
    if d == "6":
         print("Correct")
         check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    e = input ("Enter number 5 : ")
    if e == "7":
         print("Correct")
         check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    f = input ("Enter number 6 : ")
    if f == "1":
         print("Correct")
         check = True
    else:
         print("Wrong Number")
check = False
while check == False:
    g = input ("Enter number 7 : ")
    if g == "5":
         print("Correct")
         check = True
    else:
         print("Wrong Number")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    code = [7, 2, 0, 6, 7, 1, 5]
print (f"You typed in {code} into the safe")
print("The safe opened and you grabbed a key inside")
print("You added the key to your inventory and removed the code from your inventory")
Inventory.append("Key")
Inventory.remove("Code")
print(Inventory)
print("**************************************************************************************************")

print("**************************************************************************************************")
print("You hear a laugh in the distance")
print("A mysterious poison gas fills the room")
print("You feel unconscious and fall asleep")
print("**************************************************************************************************")
check = False
while check == False:
    option = input ("Type W to wake up : ")