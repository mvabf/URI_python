valor = int(input())

anos = int(valor / 365)
mes = int (valor % 365 / 30)
dias = int(valor % 365 % 30)

print(anos, "ano(s)")
print(mes, "mes(es)")
print(dias, "dia(s)")
