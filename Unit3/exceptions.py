# writ a program that ask for two numbers

def divide_two_numbers():
    try:
        x = int(input("What is the frist number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y) 
    
    except ZeroDivisionError:
        print("Connot divide by zero' try again.")
        divide_two_numbers()

    except ValueError:
        print("Please enter a valid numerica symbol, try again.")

    except:
        print("Invalid input")
        divide_two_numbers()

divide_two_numbers()

