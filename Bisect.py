import bisect
L = [10,20,20,30,40,50,60,70,90]
b = bisect

print(b.insort(L,25))
print(b.insort(L,65))
print(L)
print(b.insort_left(L,90))
print(b.insort_right(L,20))
print(L)
print(id(L[-2]))
print(id(L[-1]))
print(b.bisect(L,15))
print(b.bisect_left(L,35))
print(b.bisect_right(L,85))