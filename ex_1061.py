

diaInicial = int(input()[4:])
horaInicial, minutoInicial, segundoInicial = map(int,input().split(':'))
diaFinal = int(input()[4:])
horaFinal, minutoFinal, segundoFinal = map(int,input().split(':'))

diaTotal = diaFinal - diaInicial

horaTotal = horaFinal - horaInicial

if horaTotal < 0:
    horaTotal += 24
    diaTotal -= 1

minutoTotal = minutoFinal - minutoInicial

if minutoTotal < 0:
    minutoTotal += 60
    horaTotal -= 1

segundoTotal = segundoFinal - segundoInicial

if segundoTotal < 0:
    segundoTotal += 60
    minutoTotal -= 1

if diaTotal <= 0:
    diaTotal = 0

print("{} dia(s)".format(diaTotal))
print("{} hora(s)".format(horaTotal))
print("{} minuto(s)".format(minutoTotal))
print("{} segundo(s)".format(segundoTotal))



