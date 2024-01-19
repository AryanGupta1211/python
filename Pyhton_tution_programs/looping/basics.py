print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)



i = 1
count = 0
sum = 0
product = 1

while(i<11):
    if(i%2==0):
        count += 1
        sum += i
        product *= i
        i += 1
    else:
        i +=1

print("Count is",count)
print("Sum is",sum)
print("Product is",product)



k = 25
num = 0
sum1 = 0
while(k <= 78):
    if(k%2 != 0):
        num += 1
        sum1 += k
        k += 1
    else:
        k += 1

print(sum1)
print(num)