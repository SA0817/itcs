# arithmetic operators

name = input ("Enter your name: ")
amount = eval(input("Enter the amount to deposit: "))

print ("Hi, " + name + " , your exchange in PH denomination are as follows: ")

a = amount // 1000
b = (amount - (a * 1000)) // 500
c = (amount - (a * 1000) - (b * 500)) // 200
d = (amount - (a * 1000) - (b * 500) - (c * 200)) // 100
e = (amount - (a * 1000) - (b * 500) - (c * 200) - (d * 100)) // 50
f = (amount - (a * 1000) - (b * 500) - (c * 200) - (d * 100) - (e * 50)) // 20
g = (amount - (a * 1000) - (b * 500) - (c * 200) - (d * 100) - (e * 50) - (f * 20)) // 10
h = (amount - (a * 1000) - (b * 500) - (c * 200) - (d * 100) - (e * 50) - (f * 20) - (g * 10)) // 5
i = (amount - (a * 1000) - (b * 500) - (c * 200) - (d * 100) - (e * 50) - (f * 20) - (g * 10) - (h * 5)) // 1

print ("\nP1000 - " ,a)
print ("P500 - " ,b)
print ("P200 - " ,c)
print ("P100 - " ,d)
print ("P50 - " ,e)
print ("P20 - " ,f)
print ("P10 - " ,g)
print ("P5 - " ,h)
print ("P1 - " ,i)