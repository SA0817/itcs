triangle = eval(input("Enter number of Triangle you want: "))

for j in range(1, 6):
    for h in range(1, triangle, 1):
        for o in range(1, j + 1):
            print("*", end =" ")
        for n in range(5, j, -1):
            print(" ", end = " ")
        print(end=" ")
    print()