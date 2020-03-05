n = int(input())
resultado = 0
for i in range(1,n+1):
    if i % 2 == 0:
        resultado = pow(i,2)
        print("{}^2 = {}".format(i, resultado))
