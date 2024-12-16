user = input("Enter a name: ")
age = eval(input("Enter age: "))

if age >= 1 and age <= 7:
    print(f"Hi {user}, you are Toddler.")
elif age >= 8 and age <= 13:
    print(f"Hi {user}, you are Pre-teen.")
elif age >= 14 and age <= 18:
    print(f"Hi {user}, you are Teenager.")
elif age >= 19 and age <= 31:
    print(f"Hi {user}, you are Early Adulthood.")
elif age >= 32 and age <= 45:
    print(f"Hi {user}, you are Mid Adulthood.")
elif age >= 46 and age <= 59:
    print(f"Hi {user}, you are Port Adulthood.")
elif age >= 60 and age <= 100:
    print(f"Hi {user}, you are Senior.")
else:
    print(f"Impossible your alive, {user}!")