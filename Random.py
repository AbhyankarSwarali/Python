import random
r = random
L = [1,2,3,4,5,6,7,8]

print('Random:', r.random())
print('Uniform:', r.uniform(2,3))
print('Random integer:', r.randint(1,10))
print('Random range:', r.randrange(2,40,2))

print('')

print('Seed:-')
r.seed(10)
print('Random 1:', r.random())
print('Random 2:', r.random())
print('Random 3:', r.random())
r.seed(10)
print('Random 1.1:', r.random())
print('Random 2.1:', r.random())
print('Random 3.1:', r.random())

print('')

print('Choice:', r.choice(L))
print('Choices:', r.choices(L,k=3))
print('Sample:', r.sample(L,k=3))

print('')

print('Shuffle:-')
r.shuffle(L)
print("Shuffle:", L)

print('')

print('Get and Set:-')
st = r.getstate()
print('get 1:', r.random())
print('get 2:', r.random())
print('get 3:', r.random())
r.setstate(st)
print("set 1:", r.random())
print("set 2:", r.random())
print("set 3:", r.random())

print('')
print('Get random bits:', r.getrandbits(3))