x = "nayan"
last = len(x)-1
y = ""

for i in range(last, -1, -1):
    y += x[i]

if(y == x):
    print("It's Plaindorme")
else:
    print("Not plaindrome")


# UppeCase ASCII range: A=65, Z=90
    
# LowerCase ASCII range: a=97, z=122
    
z = "JAVA"
for i in z:
    if(ord(i)>96 and ord(i)<123):
        print(chr((ord(i) - 32)), end= "")
    elif(ord(i)>64 and ord(i)<91):
        print(chr((ord(i) + 32)), end= "")
