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
    print("2. Keep going")

    choice = input(">")

    if choice == "1":
        go_in()
    elif choice == "2":
        keep_going()


