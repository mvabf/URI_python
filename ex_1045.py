a, b, c = map(float,input().split(' '))

if a > b and a > c:
    aux = a
    a = aux
elif b > c:
    aux = a
    a = b
    b = aux
else:
    aux = a
    a = c
    c = aux

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:

    if pow(a,2) == pow(b,2) + pow(c,2):
        print("TRIANGULO RETANGULO")

    if pow(a,2) > pow(b,2) + pow(c,2):
        print("TRIANGULO OBTUSANGULO")
    
    if pow(a,2) < pow(b,2) + pow(c,2):
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

    if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print("TRIANGULO ISOSCELES")

