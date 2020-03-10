n = int(input())
media = 0
for i in range(n):
    av1, av2, av3 = map(float,(input().split(' ')))
    media = (av1 * 2.0 + av2 * 3.0 + av3 * 5.0) / 10.0
    print("%.1f" % media)
