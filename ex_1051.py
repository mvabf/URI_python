renda = float(input())

if renda <= 2000.00:
    print("Isento")
    quit()
elif renda <= 3000.00:
    imposto = (renda - 2000.00) * 0.08

elif renda <= 4500.00:
    imposto = (renda - 3000.00) * 0.18 + 1000.00 * 0.08


else:
    imposto = (renda - 4500.00) * 0.28 + 1500.00 * 0.18 + 1000.00 * 0.08

print("R$ %.2f" % imposto)
