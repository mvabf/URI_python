horaInicial, minutoInicial, horaFinal, minutoFinal = map(int,input().split(' '))

if horaInicial > 24 or horaFinal > 24:
    exit()
if horaFinal == 24 and minutoFinal > 0:
    exit()

if horaInicial < horaFinal and minutoInicial < minutoFinal:
    horaTotal = horaFinal - horaInicial
    minutoTotal = minutoFinal - minutoInicial

elif horaInicial < horaFinal and minutoInicial > minutoFinal:
    horaTotal = (horaFinal - horaInicial) - 1
    minutoTotal = 60 - (minutoInicial - minutoFinal)

elif horaInicial < horaFinal and minutoInicial == minutoFinal:
    horaTotal = horaFinal - horaInicial
    minutoTotal = minutoFinal - minutoInicial

elif horaInicial > horaFinal and minutoInicial > minutoFinal:
    horaTotal = 24 - (horaInicial - horaFinal) - 1
    minutoTotal = 60 - (minutoInicial - minutoFinal)

elif horaInicial > horaFinal and minutoInicial < minutoFinal:
    horaTotal = 24 - (horaInicial - horaFinal)
    minutoTotal = minutoFinal - minutoInicial

elif horaInicial > horaFinal and minutoInicial == minutoFinal:
    horaTotal = 24 - (horaInicial - horaFinal)
    minutoTotal = minutoFinal - minutoInicial

elif horaInicial == horaFinal and minutoInicial > minutoFinal:
    horaTotal = 24 - (horaInicial - horaFinal) - 1
    minutoTotal = 60 - (minutoInicial - minutoFinal)

elif horaInicial == horaFinal and minutoInicial < minutoFinal:
    horaTotal = horaFinal - horaInicial
    minutoTotal = minutoFinal - minutoInicial

else:
    horaTotal = 24
    minutoTotal = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horaTotal, minutoTotal))
