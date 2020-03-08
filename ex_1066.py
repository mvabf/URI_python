pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    n = int(input())

    if n % 2 == 0:
        pares += 1
        if n > 0:
            positivos +=1
        elif n < 0:
            negativos +=1
    else:
        impares+=1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1

print("{} valor(es) par(es)".format(pares))
print("{} valor(es) impar(es)".format(impares))
print("{} valor(es) positivo(s)".format(positivos))
print("{} valor(es) negativo(s)".format(negativos))
