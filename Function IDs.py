def add3(a,b,c):
    print('Inside function:', id(a), id(b), id(c))

x,y,z=10,20,30

print('Outside function:', id(x),id(y),id(z))

add3(x,y,z)
