# logical Operators 
# Arithmetic Operators + - * / // ** %
# Conmparison Operators > < >= <= ==
# Logical Operators and or !
# and means both
# or means least one


def check_eligibility(age, exp):
    if age >= 18 and exp >= 1:  # if age >= 18 and age <= 22:
        print("you are eligible")

    else:
        print("you are not eligible...")

check_eligibility()