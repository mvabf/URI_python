qtdTestes = int(input())
aux = 0
pos = 0

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in range(qtdTestes):
    saida = ''
    cifra = input()
    chave = int(input())
    for s in cifra:
        pos = alfabeto.index(s)
        aux = pos - chave # se a position for maior que a chave
        saida+= alfabeto[aux]
    print(saida)
