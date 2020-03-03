horaInicial, horaFinal = map(int,input().split(' '))

if horaInicial < horaFinal:
    horaTotal = horaFinal - horaInicial
elif horaInicial > horaFinal:
    horaTotal = 24 - (horaInicial - horaFinal)
else:
    horaTotal = 24

print("O JOGO DUROU %d HORA(S)" %horaTotal)
