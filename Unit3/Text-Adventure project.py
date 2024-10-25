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
    print("2. Go home ")
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
    print("They have all the ingredients. What do you do  ")
    print("1. pay for groceries ")
    print("2. steal")

def tomato_sauce_Spaghetti_ground_beef_parmesan_cheese():
    print("They don't HAVE INGREDIENTS. SAD ENDING ")
# end of interaction 3




    choice = input (">")
    if choice == "1":
        pay_for_groceries
    elif choice == "2":
        steal
    else:
     print("Invalid choice. Try again ")

def pay_for_groceries():
    print("you pay for the groceries. ")
    print("1. keep going")
    print("2. Go home")


def steal():
    print("You get arrested as soon as you leave the supermarket. THE BAD GUY ENDING")
# end of interaction 4




    choice = input (">")

    if choice == "1":
        Go_home 
    elif choice == "2":
        keep_going 
    else:
        print("Invalid choice. Try again")
    
def Go_home():
    print("you go home and make a cake. A THE GOOD ENDING")

def keep_going():
    print("You wander around for a while and you end up home so you go in and make a cake. A THE GOOD ENDING ")
# last interaction