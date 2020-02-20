import math

a, b = input().split(" ")

x1 = float(a)
y1 = float(b)

c, d = input().split(" ")

x2 = float(c)
y2 = float(d)

distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("%.4f" %distancia)
