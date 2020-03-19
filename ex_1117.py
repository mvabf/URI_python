contador_validas = 0
soma = 0
while contador_validas != 2:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        contador_validas+=1
        soma += nota
    else:
        print("nota invalida")

media = soma / 2.0

print("media = %.2f" % media)
