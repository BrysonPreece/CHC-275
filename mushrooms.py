option = None

while True:
    option = input("What is the size of your mushroom? Type a number or type 'quit': ").strip().lower()
    if option == "quit":
        print("Exiting the program. Goodbye!")
        break

    try:
        size = int(option)
    except ValueError:
        print("That is not a size of the mushroom or not a mushroom at all!!! HOW DARE YOU!!!!!!!!!!!")
        continue

    if size < 100:
        print("Small mushrooms are less than 100 in size")
    elif 100 <= size < 200:
        print("Medium mushrooms are mushrooms between 100 and 200 in size")
    else:
        print("That is a big boy!!! Large mushrooms are greater than or equal to 200 in size")