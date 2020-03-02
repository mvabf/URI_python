# ainda será refatorado

n = int(input())
list = []
pos = 0
for i in range(n):
    str = input()
    str2 = ''
    str3 = ''
    controle = -1
    # laço que faz o primeiro passo
    for i in str:
        aux = ord(i)
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            aux = ord(i) + 3
            str2 += chr(aux)
        else:
            str2 += chr(aux)
    # inverte a string e faz o segundo passo
    reverseString = str2[::-1]
    # pegar o index da metade da string
    halfString = int(len(str) / 2)
    
    # laço que faz o terceiro passo
    for i in reverseString:
        aux = ord(i)
        controle += 1
        if controle == halfString:
            aux = ord(i) - 1
            str3 += chr(aux)
            halfString += 1
        else:
            str3 += chr(aux)
    # insere as palavras criptografadas na lista
    list.insert(pos,str3)
    pos +=1
# imprime a lista no formato solicitado
for i in list:
    print(i)
