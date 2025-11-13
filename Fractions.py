import fractions

f1 = fractions.Fraction(1,2)
print(f1)
print('{}'.format(f1))

f2 = fractions.Fraction(0.2)
print(f2)
f2 = f2.limit_denominator(10)
print(f2)

f3 = fractions.Fraction('0.3')
print(f3)