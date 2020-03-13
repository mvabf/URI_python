casos = int(input())
aux = 0
for i in range(casos):
    x, y = map(int, input().split(' '))
    if x > y:
        aux = x
        x = y
        y = aux
    soma_impares = 0
    for n in range(x+1, y):
        if n % 2 != 0:
            soma_impares+= n
    print(soma_impares)
