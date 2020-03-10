cases = int(input())
count_rats = 0
count_frogs = 0
count_rabbits = 0
total = 0

for i in range(cases):
    str = input()
    type = str[len(str)-1:len(str)]
    quant = int(str[:len(str)-1])
    if type == 'C':
        count_rabbits += quant
    elif type == 'S':
        count_frogs += quant
    else:
        count_rats += quant

total = count_frogs + count_rats + count_rabbits

# calcular porcentagem
percent_rabbits = 100 / total * count_rabbits
percent_rats = 100 / total * count_rats
percent_frogs = 100 / total * count_frogs

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(count_rabbits))
print("Total de ratos: {}".format(count_rats))
print("Total de sapos: {}".format(count_frogs))
print("Percentual de coelhos: %.2f" % percent_rabbits + " %")
print("Percentual de ratos: %.2f" % percent_rats + " %")
print("Percentual de sapos: %.2f" % percent_frogs + " %")
