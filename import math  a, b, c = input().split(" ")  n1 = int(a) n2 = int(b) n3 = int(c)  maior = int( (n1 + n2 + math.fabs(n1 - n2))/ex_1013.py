import math

a, b, c = input().split(" ")

n1 = int(a)
n2 = int(b)
n3 = int(c)

maior = int( (n1 + n2 + math.fabs(n1 - n2)) / 2)

if maior > n3:
    print(maior, "eh o maior")
else:
    print(c, "eh o maior")
