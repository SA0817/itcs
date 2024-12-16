

for x in range(0, 11):
    print(" " * (10 - x), end = " ")
    for y in range(0, x):
        print("*" ,end=" ")
    print(x, end ="")
    for z in range (x):
        print("x", end=" ")
    print()