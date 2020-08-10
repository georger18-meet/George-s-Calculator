#Calculator Project Assignment for Y1-TA @ MEET Summer 2020.
import turtle

#Answers List.
Answ_List = []

#Calculator Screen.
SIZE_X=500
SIZE_Y=500  
turtle.setup(SIZE_X, SIZE_Y)
turtle.tracer(1,0)

#Calculator History.
t = turtle.Turtle()
t.hideturtle()
t.left(90)
t.penup()
t.goto(50,250)
t.pendown()
t.goto(50,-250)
t.penup()
t.goto(90,215)
t.write("History", font=('Courier', 20, 'bold'))
t.goto(250,210)
t.pendown()
t.goto(50,210)
t.penup()
t.goto(60,180)

#Clear Calculator History.
def btnclear():
    t.penup()
    t.goto(240,-230)
    t.pendown()
    t.goto(180,-230)
    t.goto(180,-210)
    t.goto(240,-210)
    t.goto(240,-230)
    t.penup()
    t.goto(185,-230)
    t.write("Clear", font=("Courier", 12, 'bold'))
    t.goto(60,180)

def clear(x,y):
    if x > 180 and x < 240 and y > -230 and y < -210:
        t.fillcolor("white")
        t.begin_fill()
        t.goto(55,210)
        t.goto(250,210)
        t.goto(250,-250)
        t.goto(55,-250)
        t.goto(55,210)
        t.end_fill()
        t.goto(50,210)
        t.pendown()
        t.goto(250,210)
        t.penup()
        btnclear()
        print("\nCleared History! Press Enter To Continue")
        
        
        
turtle.onscreenclick(clear, 1)
turtle.listen
btnclear()        

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

        
    except ValueError:
        print("ERROR 'Integers Only'")
        calculate()
    else:
        try:            
            operation = input("Enter Your Operation Of Choice: ")
            if operation in ('+', '-', '*', '/', '^'):

                if operation == '+':
                    Answ1 = add(x, y)
                    print("Answer:", x, "+", y, "=", Answ1)
                    Answ_List.append(Answ1)
                    hlp()

                elif operation == '-':
                    Answ2 = subtract(x, y)
                    print("Answer:", x, "-", y, "=", Answ2)
                    Answ_List.append(Answ2)
                    hlp()

                elif operation == '*':
                    Answ3 = multiply(x, y)
                    print("Answer:", x, "*", y, "=", Answ3)
                    Answ_List.append(Answ3)
                    hlp()

                elif operation == '/':
                    Answ4 = divide(x, y)
                    print("Answer:", x, "/", y, "=", Answ4)
                    Answ_List.append(Answ4)
                    hlp()

                elif operation == '^':
                    Answ5 = power(x, y)
                    print("Answer:", x, "^", y, "=", Answ5)
                    Answ_List.append(Answ5)
                    hlp()

            else:
                print("ERROR 'Invalid Operation'")
                calculate()
        except ZeroDivisionError:
            print("ERROR 'Can Not Divide By Zero'")
            calculate()
        except OverflowError:
            print("ERROR 'The Number Is Too Big For The Computer To Handle'")
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

#History List Print.
def hlp():
    for i in range(len(Answ_List)):
        ##print(Answ_List[i])
        t.write(Answ_List[i], font=('Courier', 20, 'bold'))
        Answ_List.clear()
        t.backward(25)
    
calculate()
t.mainloop()
