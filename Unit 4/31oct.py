import random
#python has four types of collections 
#tuple
#set 
#>List 
#>Dictionary

#Today, were going to focus on list
#a list is a way to store more than one vlaue in single variable
#the values in the list are called items
#items can be access by their index (position in the list) indices
#idex
best_elden_ring_weapons = ["Blasphemous","moonveil", "rivers of blood", "iron ball", "bloodhound's fang" ]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

print(best_years[0])
print(best_elden_ring_weapons[0])   #print the first item
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])   #print the last item

#list items can be changed!!!
best_elden_ring_weapons[3] = "spiked fist"
print(best_elden_ring_weapons)

#list functions()
#.pop()
# Removes a index at a given position
best_elden_ring_weapons.pop(1) #remove moonveil from the game 


#.remove()
# removes an item by value- remves first instance of the value
best_elden_ring_weapons.remove("Blasphemous") #if the value exist, it errors :(

#.append()
# adds the value as a new item to the end of the list 
best_elden_ring_weapons.append("Death's poker")

numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
print(numbers)
#.sort()
#sorts the numbers
numbers.sort()
print(numbers)
#max()
#largest number
print(max(numbers))
#min()
# smallestnumber
print(min(numbers))


