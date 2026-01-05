Inventory = []
offFlash = False
onFlash = True
option1 = True
lightoff = True
code1 = ["N0E$CAP3"]
print("Welcome to the Escape Room!!!")
try:
     file = open("Player.txt", "r")
     buffer = file.readlines()
     file.close()
except FileNotFoundError:
     buffer = []
PreviousPlayers = []
for line in buffer:
     line = line.strip()
     PreviousPlayers.append(line)
if PreviousPlayers:
    print("Previous players who have played this escape room before:")
    for player in PreviousPlayers:
         print(f"- {player}")
else:
     print("Aha! A new challenger has approached!!!")
     print("**************************************************************************************************")


try:
     name = input("Please type your name : ").strip()
except (TypeError, ValueError):
     print("Please type your name.")
finally:
     print(f"Thanks {name}, you are all set to go!!!")
     PreviousPlayers.append(name)
print("**************************************************************************************************")
file = open("Player.txt", "w")
for player in PreviousPlayers:
     file.write(f"{player}\n")
file.close()
print("**************************************************************************************************")
print("You are traveling in a train traveling to go see your grandparents for Christmas. Suddenly, you get knocked out unexpectedly by a hard object.")
print("You then fall onto the floor unconscious and you can't remember anything.")
print("You wake up tied up in a chair in the caboose of the train. You need to get to the front of the train to stop the train and escape.")
print("**************************************************************************************************")

check = False
while check == False:
    option = input("You look around the room. You see a knife on the floor. Press E to interact. : ").strip().lower()
    option ="".join(option)
    if option == "e":
        print("**************************************************************************************************")
        print("You picked up the knife to cut the rope. You are now free to move around the room.")
        print("You look around the room. There is a door with a keyhole. You need a key to escape the Caboose.")
        print("There is a painting on the wall, a shelf that is too high to reach, a beanbag, and a safe with a combination to unlock. What do you do? ")
        print("**************************************************************************************************")

        check = True
    else:
        print("That is not an option that you can do.")
        print("**************************************************************************************************")


check = False
while check == False:
    print("TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION. DO NOT INCLUDE A PERIOD")
    option1 = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. 5. Investigate the door. 6. Open Inventory : ").strip().lower()
    print("**************************************************************************************************")
    if option1 == "1":
        print("**************************************************************************************************")
        print("You investigate the safe. A combination is needed to unlock it.")
        print("**************************************************************************************************")
    elif option1 == "2":
        print("**************************************************************************************************")
        print("You investigate the shelf. It looks like something is up there that can be useful. But you can't reach it because you are only 4'1 and not 6'7.")
        print("**************************************************************************************************")
    elif option1 == "3":
        print("**************************************************************************************************")
        print("You investigate the beanbag. It looks like you found a hammer. That can be useful for breaking things.")
        print("You can use the hammer by typing the word HAMMER.")
        print("**************************************************************************************************")
        check = True
    elif option1 == "4":
        print("You Investigate the painting. It shows a picture of an old man.")
        print ("It reminds you of the book The Old Man and The Sea that you read in high school in your freshman year.")
        print("**************************************************************************************************")

    elif option1 == "5":
        print ("You investigate the door. It is a metal door that can't be broken.")
        print("You try pulling and pushing the door, but it won't budge.")
        print("You think about hitting the gym more.")
        print("**************************************************************************************************")
    elif option1 == "6":
         print(Inventory)
         print("**************************************************************************************************")

    else:
        print("That is not an option that you can do.")
check = False
while check == False:
    tool = input("Type E to use the hammer : ").strip().upper().split()
    tool = "".join(tool)
    print("**************************************************************************************************")
    if tool == "E":
        check = True
    else:
        print("That is not an option you can do.")
        print("**************************************************************************************************")


check = False
while check == False:
    option2 = input("Where would you like to use the hammer? 1. Painting, 2. Shelf, 3. Beanbag, 4. Door, 5. Safe. TYPE THE NUMBER THAT CORRESPONDS WITH THE ACTION. DO NOT INCLUDE A PERIOD. : ").strip().lower().split()
    option2 = "".join(option2)
    if option2 == "1":
            print("You use the hammer on the painting. It breaks apart and reveals a huge hole on the other side.")
            print("You step in the hole and find a ladder and a pouch that can be used for inventory.")
            print("You look on the wall and see words that say: THERE IS NO ESCAPE!!!")
            Inventory.append("ladder")
            print(Inventory)
            print("**************************************************************************************************")
            check = True

    elif option2 == "2":
            print("You try and use your hammer on the shelf but it's too high up to use.")
            print("**************************************************************************************************")

    elif option2== "3":
            print("You already searched the beanbag enough. It's usless now.")
            print("**************************************************************************************************")

    elif option2 == "4":
            print("The door is made with a hard steel.")
            print("You try and use the hammer on the door, but it's not very effective. It didn't make a dent in it.")
            print("You feel stupid because you have been playing Pokemon for 67 years now.")
            print("You should have known that steel is not very effective onto steel types or objects.")
            print("**************************************************************************************************")

    elif option2 == "5":
            print("You try and use the hammer on the safe. It does nothing to it.")
            print("**************************************************************************************************")
    else:
        print("The action you wish to do does not compute with our system.")
        print("Please try again later.")
        print("**************************************************************************************************")

check = False
while check == False:
        print("You add the Ladder to your inventory. What do you do now?")
        print("1. Check the painting. 2. Check the Shelf. 3. Check the beanbag. 4. Check the Door. 5. Check the Safe. 6. Open Inventory")
        option3 = input("Enter the number that corresponds to the action. Remember, don't type periods : ")
        print("**************************************************************************************************")

        if option3 == "1":
            print("You already inspected the painting. There is nothing to do here besides looking at that message on the wall.")
            print("The message says: THERE IS NO ESCAPE!!!")
            print("**************************************************************************************************")

        elif option3 == "2":
            print("The shelf is too high up to reach. You can reach whatever is up there with an object.")
            check = True
        elif option3 == "3":
            print("The beanbag has already been inspected.")
            print("**************************************************************************************************")

        elif option3 == "4":
            print("The door is made of steel. It won't budge without a key.")
            print("**************************************************************************************************")

        elif option3 == "5":
            print("The safe is locked. You need a code to open it.")
            print("**************************************************************************************************")

        elif option3 == "6":
            print (Inventory)
            print("**************************************************************************************************")
        else:
            print("That is not an object that you can use in your inventory.")
            print("**************************************************************************************************")
check = False
while check == False:
        option4 = input("Would you like to use an object from your inventory to climb up the shelf? (Y or N?) : ")
        print("**************************************************************************************************")

        if option4 == "Y":
            print("ok")
            print("**************************************************************************************************")
            check = True
        elif option4 == "N":
            print("Too bad")
            print("**************************************************************************************************")


check = False
while check == False:
    print(Inventory)
    option5 = input ("What object in your inventory would you like to use to climb up the shelf? : ").strip().lower().split()
    option5 = "".join(option5)

    if option5 == "ladder":
        print("You used the ladder to climb up the shelf. It looks like there is something shiny on the shelf.")
        print("You picked up a code on the shelf.")
        print("You added code to your inventory and removed Ladder from your inventory.")
        Inventory.append("code")
        Inventory.remove("ladder")
        print(Inventory)
        print("**************************************************************************************************")
        check = True

    else:
        print("Action does not compute with our system.")
        print("**************************************************************************************************")

check = False
while check == False:
    print("You have now inserted the code into your inventory.")
    print("You feel like you are almost out of here.")
    print("TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION. DO NOT INCLUDE A PERIOD")
    print("**************************************************************************************************")
    option6 = input("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. 5. Investigate the door. 6. Open Inventory : ").strip().lower()
    print("**************************************************************************************************")
    if option6 == "1":
        print("**************************************************************************************************")
        print("You investigate the safe. A combination is needed to unlock it.")
        print("**************************************************************************************************")
        check = True
    elif option6 == "2":
        print("**************************************************************************************************")
        print("You already investigated the shelf already.")
        print("**************************************************************************************************")
    elif option6 == "3":
        print("**************************************************************************************************")
        print("You already investigated the beanbag.")
        print("**************************************************************************************************")
    elif option6 == "4":
        print("You already investigated the painting already.")
        print("**************************************************************************************************")

    elif option6 == "5":
        print ("You investigate the door. It is a metal door that can't be broken.")
        print("You try pulling and pushing the door, but it won't budge.")
        print("You think about hitting the gym more.")
        print("**************************************************************************************************")
    elif option6 == "6":
         print(Inventory)
         print("**************************************************************************************************")

    else:
        print("That is not an option that you can do.")

check = False
while check == False:
    print("**************************************************************************************************")
    print("It seems the code has some writing on it.")
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
    print("Please enter the seven digits into the safe. Look at the code for clues.")
    print("**************************************************************************************************")
    check = True
check = False
while check == False:
    a = input ("Enter number 1 : ")
    if a == "3":
        print("Correct.")
        check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    b = input ("Enter number 2 : ")
    if b == "2":
         print ("Correct")
         check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    c = input ("Enter number 3 : ")
    if c == "0":
         print("Correct.")
         check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    d = input ("Enter number 4 : ")
    if d == "6":
         print("Correct.")
         check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    e = input ("Enter number 5 : ")
    if e == "7":
         print("Correct.")
         check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    f = input ("Enter number 6 : ")
    if f == "1":
         print("Correct.")
         check = True
    else:
         print("Wrong Number.")
check = False
while check == False:
    g = input ("Enter number 7 : ")
    if g == "5":
         print("Correct.")
         check = True
    else:
         print("Wrong Number.")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    code = [3,2,0,6,7,1,5]
print (f"You typed in {code} into the safe.")
print("The safe opened and you grabbed a key inside.")
print("You added the key to your inventory and removed the code from your inventory.")
Inventory.append("key")
Inventory.remove("code")
print(Inventory)
print("**************************************************************************************************")

print("**************************************************************************************************")
print("You hear a laugh in the distance.")
print("A mysterious gas fills the room.")
print("You feel unconscious and fall asleep.")
print("**************************************************************************************************")
check = False
while check == False:
    option7 = input ("Type W to wake up : ").strip().upper().split()
    option7 = "".join(option7)
    if option7 == "W":
         print("You woke up shocked as you looked around the room.")
         print("You woke up in another room of the train.")
         print("There is door that leads out of the room but it is locked.")
         print("It is dark and you can't see well.")
         print("You manage see a flashlight on the floor.")
         print("**************************************************************************************************")
         check = True
    else:
         print("Why?")
         print("**************************************************************************************************")
check = False
while check == False:
    option8 = input("Type E to interact with the flashlight : ").strip().upper().split()
    option8 = "".join(option8)
    if option8 == "E":
        print("You picked up the flashlight and can now see around the room.")
        print("But it looks like it runs on batteries and it's almost out of light.")
        print("You have got to get out of here fast!!!")
        print("**************************************************************************************************")
        option8 = input("Press E to continue : ")
        if option8 == "E":
            print("**************************************************************************************************")
            Inventory.append("flashlight")
            print(Inventory)
            check = True
    else:
        print("Brotein Shake...")

print("Suddenly you hear a voice ... It says the following: ")
print("You must unlock the door in order to continue your escape.")
print("You take a look at the lock on the wall.")
print("It is a lock that has letters on it. It looks like you have to spell a word in order to unlock the lock.")
print("**************************************************************************************************")
check = False
while check == False:
     option0 = input("Press E to continue : ").strip().upper().split()
     option0 = "".join(option0)
     if option0 == "E":
          print("Alrighty Then")
          print("**************************************************************************************************")
          check = True
     else:
          print("R U Serious?")
offMainLight = True
onMainLight = False
print("You look around the room.")
print("1. There is a light switch to turn off and on a light in the room.")
print("2. There is a chair in the room. It looks old and rusty.")
print("3. As you walk around the room, the floor creeks and makes an interesting sound.")
print("4. There is also a bookshelf in the room.")
print("5. There is also a wall.")
print("6. There is also a digital safe where you need to enter a code.")
print("**************************************************************************************************")
option9 = input("Press E to continue : ").strip().upper().split()
option9 = "".join(option9)
running = True
while running:
    print("1. Investigate the light switch.")
    print("2. Investigate the chair.")
    print("3. Investigate the floorboards.")
    print("4. Investigate the bookshelf.")
    print("5. Investigate the wall.")
    print("6. Investigate the safe.")
    print("7. Open Inventory.")
    print("**************************************************************************************************")


    option9 = input("What do you want to do? : ").strip()

    if option9 == "1":
        print("You investigate the light switch.")
        print("You flip the light switch")
        if lightoff:
             lightoff = False
             print("Light switch has been turned on.")
             print("**************************************************************************************************")

        else:
             lightoff = True
             print("Light switch has been turned off.")
             print("**************************************************************************************************")


    elif option9 == "2":
        print("You investigate the chair. It looks like an old chair with lots of rust on it.")
        choice = input("Would you like to investigate the bottom or top of the chair? (B or T) : ").strip().upper().split()
        choice = "".join(choice)
        if choice == "T":
             print("**************************************************************************************************")
             print("You investigate the top of the chair. The seat looks rusty. You probably should not sit there.")
             print("**************************************************************************************************")
        elif choice == "B":
             print("**************************************************************************************************")
             print("You investigate the bottom of the chair. There is a note on the bottom part of the chair.")
             choice1 = input("Press E to interact with the note : ").strip().upper().split()
             choice1 = "".join(choice1)
             
             if choice1 == "E":
                  print("**************************************************************************************************")
                  print("You investigate the note. It says the following:")
                  print("You are almost there. Just a few more puzzles and you will be free.")
                  print("Take this. It will help you along the way.")
                  print("From - Dr. M")
                  print("**************************************************************************************************")
                  print("You inspect the object that Dr. M gave you.")
                  print("It seems like a new flashlight. With a blacklight feature.")
                  print("You replace the old flashlight with the new one.")
                  Inventory.append("blackflashlight")
                  Inventory.remove("flashlight")
                  print(Inventory)
                  print("**************************************************************************************************")
        else:
            print("Bruh...")
            print("**************************************************************************************************")



    elif option9  == "3":
        print("You get down on your hands and knees to investigate the floorboards.")
        print("You come across a secret compartment on the wall.")
        print("But unfortunately it's locked.")
        print("Maybe there is something which can open it.")
        print("**************************************************************************************************")

        print(Inventory)
        option9 = input("What item from your inventory would you like to use? (Type quit to exit) : ").strip().lower().split()
        option9 = "".join(option9)

        if option9 == "key":
            print("**************************************************************************************************")
            print("You used the key on the secret compartment.")
            print("It opens and you grab something out of the compartment.")
            print("You received a book.")
            Inventory.append("book")
            Inventory.remove("key")
            print(Inventory)
            print("**************************************************************************************************")

        elif option9 == "quit":
            print("Ok")
            print("**************************************************************************************************")
        elif option9 == "flashlight":
             print("You tried and use the flashlight on the floorboards, but it failed.")
             print("**************************************************************************************************")

        else:
            print("Brotato Chip...")
            print("**************************************************************************************************")


    elif option9 == "4":
        print("You investigate the bookshelf.")
        print("It looks like there is a missing gap where something should go.")
        print(Inventory)
        option9 = input("What item from your inventory would you like to use? (Type quit to exit) : ").strip().lower().split()
        option9 = "".join(option9)
        if option9 == "book":
             print("**************************************************************************************************")
             print("You used the book to fill in the missing gap in the bookshelf.")
             print("The bookshelf moves to the left and reveals a hidden room.")
             print("You walk into the room and look at a book on the floor.")
             option9 = input("Press E to interact with the book : ").strip().upper().split()
             option9 = "".join(option9)
             if option9 == "E":
                  print("You picked up the book. It has the words: The Escape as the title.")
                  print("You open up the book and something falls out.")
                  print("You picked up a Master Key and added it into your inventory.")
                  Inventory.append("masterkey")
                  Inventory.remove("book")
                  print(Inventory)
                  print("**************************************************************************************************")

        elif option9 == "quit":
             print("Ok")
             print("**************************************************************************************************")

        else:
             print("Brotein Shake...")
             print("**************************************************************************************************")

    elif option9 == "5":
        print(Inventory)
        option9 = input("You investigate the wall. Would you like to use any items from your inventory on it? Type quit to exit : ").strip().lower().split()
        option9 = "".join(option9)
        if option9 == "masterkey" or option9 == "book" or option9 == "key" or option9 == "flashlight":
             print("You try to use that item from your inventory on the wall. But it failed.")
        elif option9 == "blackflashlight":
            if "blackflashlight" not in Inventory:
                print("You don't have that item.")
                print("**************************************************************************************************")

            elif lightoff:
                print("You try and use the black flashlight on the wall.")
                print(f"A code appears on the wall {code1}.")
                print("**************************************************************************************************")

            else:
                print("You try and use the black flashlight on the wall.")
                print("But it failed. The room is too bright.")
                print("**************************************************************************************************")      
    elif option9 == "6":
        print("You investigate the safe. A code is needed to unlock it.")
        option9 = input("Enter the code into the safe : ").strip()
        if option9 == "N0E$CAP3" and not lightoff:
             print(f"You entered {option9} into the safe. The safe opens and there is a big red button in the safe.")
             if "code" in Inventory:
                  Inventory.remove("code")
             option9 = input("Do you want to press the red button? (yes or no?) : ").strip().lower()
             if option9 == "yes":
                  print("**************************************************************************************************")
                  print("You press the big red button. A mysterious gas fills the room.")
                  print("You faint for hours until you get up again.")
                  print("As you look around the room, everything is gone and the walls are painted white.")
                  print("There is one final door that you must enter through, but it is locked.")
                  print(Inventory)
                  usedmaster = False
                  while not usedmaster:
                    print(Inventory)   
                    option9 = input("What item from your inventory would you like to use on this final door?").strip().lower()
                    if option9 == "masterkey":
                        print("You use the masterkey on the door. It opens and you see a staircase.")
                        print("You reach your hand out, but then you start to float upwards towards the top of the staircase.")
                        print("You see a hand reaching out for you to grab.")
                        print("As you grab the mysterious hand, everything goes black.")
                        print("**************************************************************************************************")
                        usedmaster = True
                        running = False
                        break
                    else:
                        print("YOU DID NOT USE THE MASTERKEY!!!")
                        print("Cmon man...")
                        print("**************************************************************************************************")

             elif option9  == "no":
                  print("You step back and decided not to press the button.")
                  print("You wonder what will happen if you did?")
                  print("You locked the safe back up.")
                  print("**************************************************************************************************")
             else:
                  print("You step back from the safe.")
        elif option9 == "N0E$CAP3" and lightoff:
             print("You can't see the safe in the dark.")
             print("Since you can't see, you miss-type the code.")
             print("**************************************************************************************************")


        else:
            print("The safe remains locked. Nothing happens.")
            print("**************************************************************************************************")
    elif option9 == "7":
         print(Inventory)
         print("**************************************************************************************************")

    else:
        print("Invalid option")
print(f"Thanks {name} for playing the escape room!!!")