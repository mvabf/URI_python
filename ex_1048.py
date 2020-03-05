salario = float(input())
reajuste = 0

if salario >= 0 and salario <= 400.00:
    novoSalario = salario + (salario * 0.15)
    reajuste = 15

elif salario <= 800.00:
    novoSalario = salario + (salario * 0.12)
    reajuste = 12

elif salario <= 1200.00:
    novoSalario = salario + (salario * 0.1)
    reajuste = 10

elif salario <= 2000.00:
    novoSalario = salario + (salario * 0.07)
    reajuste = 7

else:
    novoSalario = salario + (salario * 0.04)
    reajuste = 4

dif = novoSalario - salario

print("Novo salario: %.2f" % novoSalario)
print("Reajuste ganho: %.2f" % dif)
print("Em percentual: {} %".format(reajuste))
