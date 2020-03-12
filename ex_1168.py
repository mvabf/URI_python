numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input())
aux = False

def total_leds():
    total = 0
    for n in teste_list:
        if n in numeros:
            total += leds[n]
    return total


for i in range(n):
    teste = input()

    if teste[0] == 0:
        aux = True

    teste_list = [int(x) for x in str(teste)]
    if aux == True:
        teste_list.append(0)
    print(total_leds(), "leds")




