
a, b, c = input().split(' ')

aux = [int(a), int(b), int(c)]
array = [int(a), int(b), int(c)]

array.sort()


for i in array:
    print(i)

print()

for i in aux:
    print(i)
