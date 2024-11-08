# dictionary is a type of collection like a list 
# a list is a collection of items in a sequence
#a dictionary is different 
# dictionaies store data in

beau = {
    "name": "Beau",
    "age": 16,
    "city": "St. michael",
    "pets":0,
}

# each key must be unique

# retriving values from a dictionary
print(beau["name"])
print(beau["age"])

#this will error if you give a key that doesnt exist!
#print (beau[jfjj]) this errors!

#.get allows you to retrieve a calue with erroring
# when the key doesn't exist

print(beau.get("pets"))
print(beau.get("country", "country not found"))

beau["country"] = "USA"

beau["age"] = 16

beau.pop("pets")


for key, value in beau.items():
    print(key + " = " + str(value))


print(beau.keys())
print(beau.values())
print(beau.items())
print(beau.clear())