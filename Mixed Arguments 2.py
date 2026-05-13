def add(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f

r = add(2, 5, d=8, c=4, f=9, e=3)   # r=add(2,3,d=8,c=4,9,3) will give SyntaxError.
r = add(5, 2, 6, 8, f=4, e=3)   #All positional will give TypeError coz only 4 positional
print(r)