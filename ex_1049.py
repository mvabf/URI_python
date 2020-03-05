tipo = input()
grupo = input()
alimentacao = input()
animal = ''

if tipo == "vertebrado":
    if grupo == "ave":
        if alimentacao == "carnivoro":
            animal = "aguia"
        else:
            animal = "pomba"
    else:
        if alimentacao == "onivoro":
            animal = "homem"
        else:
            animal = "vaca"

else:
    if grupo == "inseto":
        if  alimentacao == "hematofago":
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        if  alimentacao == "hematofago":
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print(animal)
