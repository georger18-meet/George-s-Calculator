#Calculator Project Assignment for Y1-TA @ MEET Summer 2020.

#Defining The Calculator Operations And Their Functions.
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return x ** y



#Welcome & Instructions Text.
print("Welcome To George's Helpful Calculator!\nThe Operations That Are Available Are:")
print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Exponent(^)")
input("Press Enter to Start")



#Defining The Calculation Function, Asking For The User's Input & Error Handling.
def calculate():
    try:        
        x = float(input("\nEnter Your First Number: "))
        y = float(input("Enter Your Second Number: "))

        Answ1 = add(x, y)
        Answ2 = subtract(x, y)
        Answ3 = multiply(x, y)
        Answ4 = divide(x, y)
        Answ5 = power(x, y)
        
    except ValueError:
        print("ERROR 'Integers Only'")
        calculate()
    else:
        try:
            operation = input("Enter Your Operation Of Choice: ")
            if operation in ('+', '-', '*', '/', '^'):

                if operation == '+':
                    print("Answer:", x, "+", y, "=", Answ1)

                elif operation == '-':
                    print("Answer:", x, "-", y, "=", Answ2)

                elif operation == '*':
                    print("Answer:", x, "*", y, "=", Answ3)

                elif operation == '/':
                    print("Answer:", x, "/", y, "=", Answ4)

                elif operation == '^':
                    print("Answer:", x, "^", y, "=", Answ5)
            else:
                print("ERROR 'Invalid Operation'")
                calculate()
        except ZeroDivisionError:
            print("ERROR 'Can Not Divide By Zero'")
            calculate()
        else:
            rerun()


#Asking If The User Wants To Continue Or Stop Using The Calculator.    
def rerun():

    run_again = input("\nWould you like to calculate again?\nPlease Type Y for Yes or N for No: ")
      
    if run_again.upper() == "Y":
        calculate()

    elif run_again.upper() == "N":
        print("Good Luck!")
        quit()

    else:
        rerun()
    
calculate()
