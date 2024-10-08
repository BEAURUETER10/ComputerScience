# If statements evaluate boolean expressions! 
# they mack decisions about which code to run next

# take temperature
# print "<temperature> is hot" if its >= 80
# Otherwise, print "<temperature is not hot>"
temp = input("whats the temperature in F?\n>")
temp = int(temp)

#if <boolean expression>:
#this shoud remind of writing a function 
# def <name>():
if temp >= 80: 
    print(str(temp)  + "o is hot!")

else:       # otherwise
    print(str(temp) + "o is not hot")

# not all if statements need an else, in fact none of them need and else
#else statements are an option, they are optional 
# all else statements must have a corresponding if statement
# else statements cannot exist alone 
#an if statement can only have one else 

#Create a program that asks for a password

real_pass= "skibidi68"
input_pass= input("whats the password?\n>")
if input_pass == real_pass:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")