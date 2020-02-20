a, b = input().split(" ")

cod = int(a)
qtd = int(b)

tabela = [4.00, 4.50, 5.00, 2.00, 1.50]

total = float(qtd * tabela[cod - 1])

print("Total: R$ %.2f" % total)
