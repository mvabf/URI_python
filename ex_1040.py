
# Usando a função split, consigo extrair os valores da string e converter para ponto flutuante.
a, b, c, d = input().split(" ")
nota1 = float(a)
nota2 = float(b)
nota3 = float(c)
nota4 = float(d)

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10.0

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")

if media < 5.0:
    print("Aluno reprovado.")
    
if media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %.1f" % notaExame)
    mediaFinal = (media + notaExame) / 2.0

    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % mediaFinal)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % mediaFinal)


