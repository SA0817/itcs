input = eval(input("Enter the number of triangle(s) you want to print: "))

for j in range (1, 5):
    for r in range (1, input + 1):
        for h in range (1, j + 1):
            print ("*" , end=" ")
        for o in range (5, j, -1):
            print (" ", end=" ")
        print(end=" ")
        
    print()