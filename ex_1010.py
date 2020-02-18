a, b, c = input().split(" ")

cod1 = int(a)
qtd1 = int(b)
valor1 = float(c)

e, f, g = input().split(" ")

cod2 = int(e)
qtd2 = int(f)
valor2 = float(g)

total = qtd1 * valor1 + qtd2 * valor2

print("VALOR A PAGAR: R$ %.2f" % total)
