contImpares = 0
n = int(input())

while contImpares < 6:
    n+=1
    if n % 2 != 0:
        print(n)
        contImpares+=1
