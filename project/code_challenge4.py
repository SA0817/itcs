print("\n\nEXAMPLE")

def get_number(prompt):
    while True: 
        number = input(prompt)
        if number.replace('.', '', 1).isdigit() or (number[0] == '-' and number[1:].replace('.', '', 1).isdigit()):
            return int(number)  
        else:
            print("Invalid input! Please enter a valid number.")

while True:
    number1 = get_number("Enter a number --> ")
    number2 = get_number("Enter another number --> ")
    
    answer1 = number1 + number2
    answer2 = number1 - number2
    answer3 = number1 * number2
    answer4 = number1 / number2 if number2 != 0 else "undefined (division by zero)"
    answer5 = number1 % number2 if number2 != 0 else "undefined (modulus by zero)"
    answer6 = number1 ** number2
    answer7 = number1 // number2 if number2 != 0 else "undefined (floor division by zero)"

    print("The sum of ", number1, " + ", number2, " is ", answer1)
    print("The difference of ", number1, " and ", number2, " is ", answer2)
    print("The product of ", number1, " and ", number2, " is ", answer3)
    print("The quotient of ", number1, " and ", number2, " is ", answer4)
    print("The remainder of ", number1, " and ", number2, " is ", answer5)
    print("The exponent of ", number1, " and ", number2, " is ", answer6)
    print("The floor division of ", number1, " and ", number2, " is ", answer7)
    
    while True:  
        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if choice == "yes":
            break  
        elif choice == "no":
            print("Thank you for your time. Goodbye!")
            exit()  
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")