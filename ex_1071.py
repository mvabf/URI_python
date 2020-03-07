x = int(input())
y = int(input())
impares = 0
if x > y:
    for i in range(y+1,x):
        if i % 2 != 0:
            impares = impares + i
else:
    for i in range(x+1, y):
        if i % 2 != 0:
         impares +=i
print(impares)
