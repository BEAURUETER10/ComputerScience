# there a couple types of loops python
# the for loop lets you iterate througha list 
# great for looping a set number times 
# but what if we need to loop an uncertain number of times 
#ex enering your password
# you cold get it right the fries
# or anything in between



real_pass = "ninjalowtaper"
enterd_pass = ""

attempts = 0

while enterd_pass != real_pass:
    #ask for the password
    enterd_pass = input("Please enter the password\n>")
    attempts = attempts + 1
    #check if password is correct
    if enterd_pass == real_pass:
        print("ACCESS GRANDTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + "attempts")
        print("try again")

print("welcome!")

# with while loops, you need to be careful for infinite loops
#when you put your computer into rest mode , it has nightmares about infinite loops /joke
#like black holesw 
# Don't create a black hole
# lets create a black hole

count = 0
while True:
    count = count + 1
    print(count)

#real world exmple

user_input = ""

while user_input != "exit":
    user_input = input("enter somthing!")
    print("type 'exit' to quit" )
    print("you typed: " + user_input)

print ("All done")