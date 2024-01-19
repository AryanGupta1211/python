
# start , stop, skip (n-1 times) 
for i in range(0,11):
    print(i)

count = 0
sum = 0
prod = 1
for i in range(25,79,2):
    count += 1
    sum += i
    prod *= i

print(count)
print(sum)
print(prod)


