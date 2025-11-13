import fractions

f1 = fractions.Fraction(1,2)
f2 = fractions.Fraction(0.2)
f2 = f2.limit_denominator(10)

print('{}'.format(f1 + f2))
print('{}'.format(f1 - f2))
print('{}'.format(f1 * f2))
print('{}'.format(f2 / f1))

print('Numerator of f1:', f1.numerator)
print('Denominator of f2:', f2.denominator)