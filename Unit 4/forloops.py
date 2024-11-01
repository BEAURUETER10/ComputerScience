# for loops
# this is BIG deal
# for loops allow the programmer to repeat' or what we call loop

#write a program that prints the numbes 1 through 10
#each on a new line 

fav_foods = ["eggs bennedict","Fried chicken", "Mac n Cheese"]

#for <var> in <list>:

for i in range(90,101):  
    print(i)

for food in fav_foods:
    print(food)
    #runs all of the lines inside the for loop
    #when it reachs the bottom the list, it runs again
    #and moves on to the next item in the list
    #it ends when there are no list items left


for i in range(10,0,-1): #start, stop, step
    print(i)

#sum of a list

nums = [68, 70, 419, 421, 665]
sum = 0
for n in nums:
    sum = sum + n

print(sum)


#square of each number

ints = [3,2,5,4,1]
newlist = []

for i in ints:
    newlist.append(i*i)

print(newlist)

#character count

stringy = input("Please enter a string \n>")
numvawels = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvawels = numvawels = 1

print(numvawels)

#print multiplication tablel

try:
    multi = int(input("gimme an int yo \n>"))
except:
    print("womp womp")

for i in range(0,multi+1):
    print(str(multi) + "x" + str(i)+ "=" + str (multi*i))


# list of names
names = ["peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello, " + name + "!")