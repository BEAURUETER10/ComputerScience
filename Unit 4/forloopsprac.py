# for loops review
#For loops allow us to us to iterate through a list!
#iterate: perform repeatedly
# to do something repatedly 
# to look at every item in a list, one by one 


#basic syntax
#syntax: the grammar of code 

pokemon_cards= ["squirtle", "bidoof","zigagoon","charzard"]

for card in pokemon_cards:
    print("the next card is...")
    print(card)

route = ["Home", "Taco Bell", "the park", "goodwill","home"]


#if you need to look at multple list items during the one iteration,
#doing for item in list dosint work
#for item in list only allows you to access one list item per iteration
for location in route:
    print("you are traveling from"+ location + "to" + route[1])
    #this doesnt work!

#if you need to access multiple list 

for i in range(0,len(route)): #creates a list [0, 1, 2, 3, 4,]


 
    try:
        print(":you are traveling from " + route[i] + "to" + route[i+1])
    except:
        print("route finished!")