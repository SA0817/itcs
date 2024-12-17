def start_program():
    name = input("Enter your name to start: ")
    print(f"Hi! Welcome {name}, do you want to continue the program? (yes/no)?", end=" ")
    proceed = input().lower()
    while True:
        if proceed == "yes":
            main_menu(name)
            break
        elif proceed == "no":
            print("Thank you for your time. Goodbye!")
            break
        else:
            print("Invalid option, Please try again.")
            proceed = input()


def main_menu(name):
    while True:
        print("\n\n=================================")
        print("\nMAIN MENU")
        print("\n1. Printing in Python")
        print("2. Operators")
        print("3. Variables in Python")
        print("4. Conditional")
        print("5. Loops")
        print("6. Functions")
        print("7. Lists")
        print("8. Exit")
        print("\n=================================")
        choice = input("Choose a topic you want to discuss: ")
       

        if choice == "1":
            printing_in_python()
        elif choice == "2":
            operators()
        elif choice == "3":
            variables_in_python()
        elif choice == "4":
            conditional_in_python()
        elif choice == "5":
            loops_in_python()
        elif choice == "6":
            functions_in_python()
        elif choice == "7":
            lists_in_python()
        elif choice == "8":
            print(f"Thank you for learning, {name}! Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")


# PRINTING IN PYTHON
def printing_in_python():
    while True:
        print("\n\n=================================")
        print("\nPrinting in Python")
        print("\nPrinting is used to display output in\nPython using the `print()` function.")
        print("\n1. Simple Printing")
        print("2. New Line")
        print("3. Back to main menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n\n=================================")
            print("\nInput:")
            print('print("Hello, World!")')
            print("\nOutput:")
            print("Hello, World!")
            print("\nExplanation: The `print()` function\ndisplays text or data inside the parentheses.\nStrings are enclosed in quotes.")
            print("\n1. Back to Printing in Python")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")
                
        elif choice == "2":
            print("\n\n=================================")
            print("\nInput:")
            print('print("Hello\\nWorld")')
            print("\nOutput:")
            print("Hello")
            print("World")
            print("\nExplanation: The `\\n` is a newline\ncharacter that moves the output to the\nnext line.")
            print("\n1. Back to Printing in Python")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")
        
        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose a valid option.")


# OPERATORS
import subprocess
def operators():
    while True:
        print("\n\n=================================")
        print("\nOperators")
        print("\nOperators are symbols that perform operations\non variables and values. These operations can\ninvolve arithmetic, assignment and more.")
        print("\n1. Arithmetic")
        print("2. Assignment")
        print("3. Back to main menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":  
            print("\n\n=================================")
            subprocess.run(["python", "project/code_challenge4.py"])
            print("\n=================================")
            
        elif choice == "2":
            print("\n\n=================================")
            subprocess.run(["python", "project/assignment.py"])
            print("\n=================================")

        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose a valid option.")


# VARIABLES IN PYTHON
import subprocess
def variables_in_python():
    while True:
        print("\n\n=================================")
        print("\nVariables in Python")
        print("\nVariables are used to storeata\nvalues, like numbers, text, or other objects.")
        print("\n1. Example")
        print("2. Explanation")
        print("3. Back to main menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n\n=================================")
            subprocess.run(["python", "project/activity3.py"])
            print("\n=================================")

        elif choice == "2":
            print("\n\n=================================")
            print("\nExplanation:")
            print("A variable is like a container for data.\nYou name it and assign a value, which can\nlater be used in your program.")
            print("\n1. Back to Variables in Python")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")

        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose a valid option.")


# CONDITIONAL
import subprocess
def conditional_in_python():
    while True:
        print("\n\n=================================")
        print("\nConditional in Python")
        print("\nConditional statements are an essential\npart of programming in Python.") 
        print("They allow you to make decisions based\non the values of variables or the result\nof comparisons.")
        print("\n1. Conditional Statement")
        print("2. Conditional Operators")
        print("3. Back to main menu")
        print("\n=================================")
        choose = input("Choose an option: ")

        if choose == "1":
            print("\n\n=================================")
            subprocess.run(["python", "project/activity9.py"])
            print("\n=================================")
           
        elif choose == "2":
            print("\n\n=================================")
            print("\nPython Conditions and If statements")
            print("Python supports the usual logical\nconditions from mathematics:")
            print("""\nEquals: a == b
                    Not Equals: a != b
                    Less than: a < b
                    Less than or equal to: a <= b
                    Greater than: a > b
                    Greater than or equal to: a >= b""")
            print("\n1. Back to Conditional in Python.")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")

        elif choose == "3":
            break
                
        else:
            print("Invalid input. Please choose a valid option.")


# LOOP
def loops_in_python():
    while True:
        print("\n\n=================================")
        print("\nLoops in Python")
        print("\nLoops are used to repeat a block of code\nmultiple times.")
        print("\n1. For Loop")
        print("2. While Loop")
        print("3. Back to main menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n\n=================================")
            print("\nInput:")
            print("for junas in range(1, 11):\nprint('Pogi si Junas')")
            print("\nOutput:")
            print("Pogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas\nPogi si Junas")
            print("\n1. Back to Loops in Python.")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")

        elif choice == "2":
            print("\n\n=================================")
            print("\nInput:")
            print("x = 1\nwhile x <= 3:\n    print(x)\n    x += 1")
            print("\nOutput:")
            print("1\n2\n3")
            print("\nExplanation: A `while` loop runs as long\nas the condition is true. It checks the condition\nbefore each iteration.")
            print("\n1. Back to loops in Python.")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("\nInvalid choice. Please try again.")
                    sub_choice = input("Choose an option: ")

        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose a valid option.")


# FUNCTION
def functions_in_python():
    while True:
        print("\n\n=================================")
        print("\nFunctions in Python")
        print("\nFunctions are reusable blocks of code that perform specific tasks.")
        print("\n1. Example")
        print("2. Explanation")
        print("3. Back to main menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n\n=================================")
            print("\nInput:")
            print("def greet():")
            print("     print('Hello! Welcome to Python.')\n\ngreet()")
            print("\nOutput:")
            print("Hello! Welcome to Python.")
            print("\nExplanation: Functions are defined with\n`def`, followed by a name. Call the function\nto execute it.")
            print("\n1. Back to Functions in Python.")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("Invalid choice, Please try again.")
                    sub_choice = input("Choose an option: ")
        
        elif choice == "2":
            print("\n\n=================================")
            print("\nExplanation:")
            print("A function is a block of code that you\ndefine once and reuse multiple times by\ncalling its name.")
            print("\n1. Back to Functions in Python.")
            print("\n=================================")
            sub_choice = input("Choose an option: ")
            while True:
                if sub_choice == "1":
                    break
                else:
                    print("Invalid choice, Please try again.")
                    sub_choice = input("Choose an option: ")
            
        elif choice == "3":
            break
        else:
            print("Invalid input. Please choose a valid option.")


# LIST
def lists_in_python():
    my_list = []

    while True:
        print("\n\n=================================")
        print("\nLists in Python")
        print("\n1. Access list")
        print("2. Add to list")
        print("3. Remove from list")
        print("4. Back to Main Menu")
        print("\n=================================")
        choice = input("Choose an option: ")

        if choice == "1":
            if not my_list:
                print("The list is empty!")
            else:
                print("Current List:", my_list)

        elif choice == "2":
            item = input("Enter an item to add: ")
            my_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == "3":
            if not my_list:
                print("The list is empty! Nothing to remove.")
            else:
                print("Current List:", my_list)
                item = input("Enter the item to remove: ")
                if item in my_list:
                    my_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' is not in the list.")

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please choose a valid number.")

start_program()