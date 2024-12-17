# ASSIGNMENT OPERATORS
print("\n\nEXAMPLE")

while True:
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
    choice =input("\nDO you want to try again? (yes/no) ").lower()
    if choice == "yes":
        continue
    elif choice == "no":
        print("Thank you for using the program.")
        break