#create diamond shape using numbers
#sanagustin_code_challenge13.py

for a in range (1, 6):
    for b in range (6, a, -1):
        print (" ", end = " ")
    for c in range (a, 1, -1):
        print (c, end = " ")
    for d in range (1, a + 1):
        print (d, end = " ")
 
    print ()

for e in range (4, 0, -1):
    for f in range (6, e, -1):
        print (" ", end = " ")
    for g in range (e, 0, -1):
        print (g, end = " ")
    for h in range (2, e + 1):
        print (h, end = " ")

    print ()