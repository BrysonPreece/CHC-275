print("Welcome to the Escape Room!!!")
print("You are traveling in as train traveling to go see your grandparents for Christmas. Suddenly, you get knocked out unexpectedly by a hard object.")
print("You then fall onto the floor unconscious and you can't remember anything.")
print("You wake up tied up in a chair in the caboose of the train. You need to get to the front of the train to stop the train and escape.")
check = False
while check == False:
    option = input("You look around the room. You see a knife on the floor. Press P to pick up the knife. ").strip().lower().split()
    option = "".join(option)
    if option == "p":
        print ("**************************************************************************************************")
        print("You picked up the knife to cut the rope. You are now free to move around the room.")
        print("You look around the room. There is a door with a keyhole. You need a key to escape the Caboose.")
        print("There is a painting on the wall, a shelf that is too high to reach, a beanbag, and a safe with a combination to unlock. What do you do? ")
        print("1. Investigate the safe, 2. Investigate the shelf, 3. Investigate the beanbag, 4. Investigate the painting. TYPE THE NUMBER THAT CORRESPONDS TO THE ACTION")
        print ("**************************************************************************************************")
    check = True