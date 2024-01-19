num = 8
check = True

for i in range (2, num):
    if(num % i == 0):
        check = False

if(check == False):
    print("Not Prime")
else:
    print("Prime")


count = 0
sum = 0
for i in range(13, 49):
    num1 = i
    check = True
    for i in range (2, num1):
        if(num1 % i == 0):
            check = False

    if(check == True):
        count += 1
        sum += num1

print(count)
print(sum)