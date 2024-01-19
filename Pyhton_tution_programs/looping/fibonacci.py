x = 0
y = 1

print(x)
print(y)

for i in range(1,11):
    x,y = y, (x+y)
    print(y)