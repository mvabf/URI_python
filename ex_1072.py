testes = int(input())
dentro = 0
fora = 0

for i in range(testes):
    n = int(input())
    if n >= 10 and n <= 20:
        dentro += 1
    else:
        fora += 1

print("{} in".format(dentro))
print("{} out".format(fora))
