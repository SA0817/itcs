isBuy = input("Do you want to make a grocery purchase (yes/no): ")

if isBuy.lower() == "yes" :
	 item_name = input("Enter the item name: ")
	 item_price = eval(input("Enter the price of the item: "))
	 age = eval(input("Enter your age: "))
	 cash = eval(input("Enter the amount of cash you have given: "))

	 discount_amount = round(item_price * 0.052, 2)
	 discount_price = round(item_price - discount_amount, 2)
	 tax_amount = round(item_price * 0.123, 2)
	 tax_price = round(item_price + tax_amount)

	 if age >= 60:
	 	 print(f"\nHi, our dear customer, you purchased a/an {item_,name}, that costs {item_price}Php plus a 5.2% discount {discount_amount}Php to your total purchase. ")
	 	 print(f"Total: {round(item_price - discount_amount, 2)} ")
	 	 print(f"Change: {round(cash - discount_price, 2)} ")
	 	 print("Thank you for shopping, see you next time! ")

	 elif age >=18:
	 	 print(f"\nHello!, you have purchased {item_name}, that costs {item_price}Php plus a 12.3% tac {tax_amount}Php to your total purchase. ")
	 	 print(f"Total: {round(item_price + tax_amount, 2)} ")
	 	 print(f"Change: {round(cash - tax_price, 2)} ")
	 	 print("Thank you for shopping, see you next time! ")

else:
	 print("\nThank you for shopping with us! We hope to see you again.")
