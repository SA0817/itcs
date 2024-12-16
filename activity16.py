#for loop complete range
for j in range(1, 6):
    for h in range(1, j + 1):
        print(" ", end = " ")
    for o in range(6, j, -1):
        print("*", end = " ")
    print()