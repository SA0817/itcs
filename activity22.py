#function

import os
def activity2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print (num1, "Floor Divide to", num2, "=", num1//num2)
    
def activity4():
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter anothoer number: "))
    answer = num1 + num2

    print ("The sum of", num1, " + ", num2, " is ", answer)

def activity5():
    print("FARENHEIT TO CELSIUS CONVERTER PROGRAN")
    farenheit = eval(input("Enter the temperature in Farenhiet: "))
    celcius = ((farenheit - 32) * 5)/9
    print (f"{farenheit}, degrees Farenheit converter to celsius is {round(celcius, 2)} degrees")

def activity6():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print (x)

    x = x + 20

    print (x)

    X = x + 25

    print (x)

    x = x + 30

    print (x)

isContinue = True
while isContinue:
    ask = input("Select the python file you want to open: \n1.) activity2 \n2.) activity4 \n3.) activity5 \n4.) activity6 \n5.) exit \nInput: ")
    os.system('cls')
    if ask == "1":
        print("Program is running")
        activity2()
    elif ask == "2":
        print("Program is running")
        activity4()
    elif ask == "3":
        print("Program is running")
        activity5()
    elif ask == "4":
        print("Program is running")
        activity6()
    elif ask == "5":
        break
    else:
        continue