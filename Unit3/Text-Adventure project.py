# I don't know what im doing.
# Please skip this if you are playing.
# Thank you.




def start_adventure():
    print("You stand by the door of your home. what do you do?")
    print("1. Stay home")
    print("2. Go out")

    choice = input(">") 

    if choice == "1":
        stay_home()
    elif choice == "2":
        go_out()
    else:
        print("Invalid choice. Try again")

def stay_home():
    print("you dicide to stay home. THE LAZY ENDING. ")

def go_out():
    print("You go out on the street and walk to the supermarket ")
    print("1. Go in")
    print("2. Keep going ")
# end of frist interaction




    choice = input(">")

    if choice == "1":
        go_in()
    elif choice == "2":
        go_home()
    else: print("Invalid choice. Try again ")

def go_in():
    print("You go in the supermarket. what do you get? ")
    print("1. egg, milk, flour, and cocoa ")
    print("2. tomato sauce, Spaghetti, ground beef, and parmesan cheese ")


def go_home():
    print("you go home. NOT TODAY ENDING")
# end of 2 interaction

    choice = input(">")
    if choice == "1":
        egg_milk_flour_cocoa()
    elif choice == "2":
        tomato_sauce_Spaghetti_ground_beef_parmesan_cheese()
    else:
        print("Invalid choice. Try again ")

def egg_milk_flour_cocoa():
    print("")

def tomato_sauce_Spaghetti_ground_beef_parmesan_cheese():
    print("")