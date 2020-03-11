list = []
maior = 0
for i in range(100):
    n = int(input())
    list.append(n)
    if list[i] > maior:
        maior = list[i]

print(maior)
print(list.index(maior) + 1)
