#looptermination
#codechallenge14.py
#sanagustin


total = 0

while True:
    number = eval(input("Please enter a number: "))

    if number == 0:
        print("Loop Terminated")
        print(f"The sum of all the numbers is {total}")
        break
    else:
        print("Please continue entering a number")
        total += number
