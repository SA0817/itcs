#arrow up using asteris
#sanagustin_code_challenge12.py

for a in range (1, 6):
    for b in range (6, a, -1):
        print (" ", end = " ")
    for c in range (1, a+1):
        print ("*", end = " ")
    for d in range(1, a):
        print ("*", end = " ")
        
    print ()
    
for e in range(1, 5):
    print ("", end = " ")
    for f in range (1, 5):
        print (" ",end = " ")
    for g in range(1,3):
        print ("*", end = " ")
 
    print()