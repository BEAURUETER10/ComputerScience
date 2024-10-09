# the if statement has two buddies
# the first little buddy is the else statement

x = 10

if x > 0:   # not every if needs an else
    print("x is a positibe number")

# the second little buddy is the elif (else if)
elif x < 0:
    print("x is a negative number")

else:   # else always needs an if
    print("x is a zero")



light = input("what color is the light?\n")

if light.lower() == "green":
    print("go")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP") 
