import math

a, b, c = input().split(" ")

A = float(a)
B = float(b)
C = float(c)
delta = 0

if A == 0 or B == 0 or C == 0:
    print("Impossivel calcular")
else:
    delta = pow(B,2) - 4 * A * C

    if delta < 0:
        print("Impossivel calcular")

    else:
        x1 = (-B + math.sqrt(delta) ) / (2 * A)
        x2 = (-B - math.sqrt(delta) ) / (2 * A)

        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
    

