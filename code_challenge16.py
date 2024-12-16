#BANK SIMULATION PROGROM
#code_challenge16.py
#sanagustin


accounts = {}

while True:
    print("\n1. Create Bank Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter account name: ")
        if name in accounts:
            print("Account already exists.")
        else:
            deposit = float(input("Enter initial deposit: "))
            accounts[name] = deposit
            print(f"Account created for {name} with balance: {deposit}")
    
    elif choice == '2':
        name = input("Enter account name: ")
        if name in accounts:
            deposit = float(input("Enter deposit amount: "))
            accounts[name] += deposit
            print(f"Deposited {deposit}. Current balance: {accounts[name]}")
            balance = accounts[name]
            print("Denomination breakdown:")
            for d in [1000, 500, 200, 100, 50, 20, 10, 5, 1]:
                if balance >= d:
                    print(f"{d} PHP: {int(balance // d)}")
                    balance %= d
        else:
            print("Account does not exist.")
    
    elif choice == '3':
        name = input("Enter account name: ")
        if name in accounts:
            withdraw = float(input("Enter withdrawal amount: "))
            if withdraw > accounts[name]:
                print("Insufficient balance!")
            else:
                accounts[name] -= withdraw
                print(f"Withdrew {withdraw}. Current balance: {accounts[name]}")
                balance = accounts[name]
                print("Denomination breakdown:")
                for d in [1000, 500, 200, 100, 50, 20, 10, 5, 1]:
                    if balance >= d:
                        print(f"{d} PHP: {int(balance // d)}")
                        balance %= d
        else:
            print("Account does not exist.")
    
    elif choice == '4':
        name = input("Enter account name: ")
        if name in accounts:
            print(f"Current balance for {name}: {accounts[name]}")
        else:
            print("Account does not exist.")
    
    elif choice == '5':
        print("Thank you, goodbye")
        break
    
    else:
        print("Invalid option. Please try again.")