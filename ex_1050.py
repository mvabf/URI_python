n = int(input())
ddd = [61, 71, 11, 21, 32, 19, 27, 31]
cidades = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
indice = -1

for i in ddd:
    if i == n:
        indice = ddd.index(i)

if indice >= 0:
    print(cidades[indice])
else:
    print("DDD nao cadastrado")
