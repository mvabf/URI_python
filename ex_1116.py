n = int(input())


for i in range(n):
    primeiro_numero, segundo_numero = map(int, input().split(' '))

    if segundo_numero == 0:
        print("divisao impossivel")
    else:
        print(primeiro_numero / segundo_numero)
