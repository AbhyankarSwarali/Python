import fractions
L = [(1,2), (4,9), (6,8)]

for num, deno in L:
    print('{}'.format(fractions.Fraction(num,deno)))