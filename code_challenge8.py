#acquiring 10 numbers and get the summation of all the numbers


sum = 0
for x in range(1, 11):
    num = eval(input(f"Enter a number #{x}  :   "))
    sum += num
    
    
print(f"The sum of all the numbers given is {sum}")