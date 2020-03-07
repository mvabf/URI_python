n, teste = map(int, input().split(' '))
while not(n == 0 and teste == 0):

    #int to list
    digits = [int(x) for x in str(teste)]
    while n in digits:
        digits.remove(n)
    # caso a lista fique vazia
    if len(digits) == 0:
        digits = [0]

    # list to string depois to integer
    strings = [str(integer) for integer in digits]
    join_string = "".join(strings)
    digits_int = int(join_string)

    # output
    print(digits_int)

    n, teste = map(int, input().split(' '))



