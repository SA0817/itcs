#trianglepattern
#codechallenge15.py
#sanagustin


import os

count = 0

while True:
    question = input("Do you want to create more triangles (yes or no)?: ").lower()

    if question == "no":
        os.system("cls")
        print("Program is Terminated")
        break
    elif question == "yes":
        os.system("cls")
        count += 1
        for x in range(1, 6):
            for r in range(count):
                print("* " * x + "  " * (5 - x), end="")
            print()
    else:
        os.system("cls")
        print("Invalid Answer\nPlease respond with 'yes' or 'no'.")