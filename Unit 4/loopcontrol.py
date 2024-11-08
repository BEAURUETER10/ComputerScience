# loop control statements 
# Allow you to change how loops operate
#they do things like quit the loop early, skip the current loop or even do nothing at all
#braeak continue pass

#bresk
#exits a loop prematurely before it was supposed to end
# happens immediately when ran
# program contnues where the loop ended

#example

bag_of_fruit = ["apple", "orange", "bug", "kiwi" ]

for fruit in bag_of_fruit:
    if fruit == "bug":
        print("you found a nasty bug")
        break
    else:
        print("you ate a" + fruit)

print("all done")

# continue
# skips the current loop 
# it does exit the entre loop[ just moves on to the next iteraton

#example
orders = [15, 30, 35, 23, 100, 3, 10, 22]

#discount applying programs
#only applt discount for orders above $20

for order in orders:
    if order <20:
        continue
    print("$" + str(order) + "order discounted 5% to $"+ str(order * 0.95))


#pass

def enter_forest():
    pass

def swim_river():
    pass

