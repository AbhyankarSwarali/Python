import math

print('Ceil:', math.ceil(12.3))
print('Floor:', math.floor(12.7))

print('Absolute of negative:', math.fabs(-1.45))
print('Absolute of positive:', math.fabs(1.22))

print('Modulus:', math.fmod(13,2))
print('Remainder 1:', math.remainder(13,5))
print('Reaminder 2:', math.remainder(16,3))

print('Perfect Square root:', math.sqrt(36))
print('Square root:', math.sqrt(13))
print('Integer square root:', math.isqrt(13))
print('Power:', math.pow(2,3))
print('Factorial:', math.factorial(5))

print('GCD:', math.gcd(35,21))
print('LCM:', math.lcm(27,18))
print('Permutation:', math.perm(5,2))
print('Combination:', math.comb(5,2))

print('Product:', math.prod([1,2,3,4,5]))
print('Sum:', math.fsum([1,2,3,4,5]))

print('Radians:', math.radians(30))
print('Degrees:', math.degrees(3.1415))

print('Sine:', math.sin(30))  # Input is in radians
print('Sine hyperbolic:', math.sinh(5))
print('Cosine:', math.cos(30))
print('Cosine hyperbolic:', math.cosh(3))
print('Tangent:', math.tan(45))
print('Tangent hyperbolic:', math.tanh(15))

print('Natural log:', math.log(10))
print('Log base 2:', math.log2(256))
print('Log base 10:', math.log10(5))

# Built-in constants
print('Pi value:', math.pi)
print('e value:', math.e)
print('Infinity:', math.inf)
print('Not a number (NAN):', math.nan)