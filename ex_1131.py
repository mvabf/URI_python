total_partidas = 0
total_vitorias_inter = 0
total_vitorias_gremio = 0
total_empates = 0
op = 1
msg = ''
while op == 1:
    gol_inter, gol_gremio = map(int, input().split(' '))

    total_partidas+=1

    if gol_inter > gol_gremio:
        total_vitorias_inter+=1
    elif gol_inter < gol_gremio:
        total_vitorias_gremio+=1
    else:
        total_empates +=1
    print("Novo grenal (1-sim 2-nao)")
    op = int(input())


if total_vitorias_gremio > total_vitorias_inter:
    msg = "Gremio venceu mais"
elif total_vitorias_inter > total_vitorias_gremio:
    msg = "Inter venceu mais"
else:
    msg = "Nao houve vencedor"

print("{} grenais".format(total_partidas))
print("Inter:{}".format(total_vitorias_inter))
print("Gremio:{}".format(total_vitorias_gremio))
print("Empates:{}".format(total_empates))
print(msg)
