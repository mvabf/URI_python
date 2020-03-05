x, y = map(float,input().split(' '))

if x > 0 and y > 0:
    quadrante = "Q1"

elif x < 0 and y > 0:
    quadrante = "Q2"

elif x < 0 and y < 0:
    quadrante = "Q3"

elif x > 0 and y < 0:
    quadrante = "Q4"

elif x == 0 and (y > 0 or y < 0):
    quadrante = "Eixo Y"

elif y == 0 and (x > 0 or x < 0):
    quadrante = "Eixo X"

else:
    quadrante = "Origem"

print(quadrante)
