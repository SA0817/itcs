#diamond asteris
#sanagustin_code_challenge10.py

for a in range (1, 7):
    for b in range (7, a, -1):
        print (" ", end = " ")
    for c in range (1, a + 1):
        print ("*", end = " ")
    for d in range (1, a):
        print ("*", end = " ")
         

    print ()

    
for e in range (1, 7):
    for f in range (1, e + 1):
        print (" ", end = " ")
    for g in range (7, e + 1, -1):
        print ("*", end = " ")
    for h in range (7, e, -1):
        print ("*", end = " ")
        
    print ()