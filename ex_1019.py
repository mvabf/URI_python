valor = int(input())

horas = int( valor / 3600)
minutos = int(valor % 3600 / 60)
segundos = int(valor % 3600 % 60)
output = ("{}:{}:{}").format(horas, minutos, segundos)
print(output)
