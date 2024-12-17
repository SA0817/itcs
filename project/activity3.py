
while True:
    print("\n\nEXAMPLE")
    Fullname = input("\nFullname: ")
    Age = input("Age: ")
    Birthdate = input("Birthdate: ")
    Birthplace = input("Birthplace: ")
    Gender = input("Gender: ")
    Nationality = input("Nationality: ")
    MaritalStatus = input("Marital Status: ")
    Religion = input("Religion: ")
    Address = input("Address: ")
    ContactNumber = input("Contact Number: ")
    EmailAddress = input("Email Address: ")
    Skills = input("Skills: ")
    Languages = input("Languages Spoken: ")
    Hobbies = input("Hobbies: ")

    print("\nBio-data Information")
    print("====================")
    print("My name is " + Fullname + ", I was born on " + Birthdate + " in " + Birthplace + ". " + "I am " + Age + " years old, " + "I am a " + Gender + " " + Nationality + ". " + "I am currently " + MaritalStatus + " and I follow the " + Religion + " religion. " + "I live at " + Address + ", my contact number is " + ContactNumber + " or " + "you can reach me at " + EmailAddress + ". " + " My skills include " + Skills + ". " + "I can speak " + Languages + ", and in my free time, I enjoy " + Hobbies + ".")
    while True:
        choice = input("\nDo you want to enter another bio-data? (yes/no): ").lower()
        if choice == "yes":
            break  
        elif choice == "no":
            print("Thank you for your time. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")