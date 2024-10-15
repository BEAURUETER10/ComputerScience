# Create a function called free_shipping 
# that tells you if you qualify for free shipping 
# you only get free shipping if 
# you are a prime member OR order is at least $25
# you are at least 18 years old OR have parent 


def check_eligibility(age):
    if age >= 18:
        print("you qualify for free shipping")
    
    else:
        print("you do not qualify for free shipping")


check_eligibility()