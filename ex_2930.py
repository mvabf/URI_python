a, b = input().split(" ")

dia_entregue = int(a)
prazo = int(b)

aux = prazo - dia_entregue

if aux < 0:
    print("Eu odeio a professora!")
if aux >= 3:
    print("Muito bem! Apresenta antes do Natal!")
if aux >= 0 and aux < 3:
    print("Parece o trabalho do meu filho!")
    prazo+=2
    if prazo <= 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")
