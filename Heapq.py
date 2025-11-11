import heapq
h = heapq

print(type(h))
H = []

print(h.heappush(H,20))
print(h.heappush(H,50))
print(h.heappush(H,10))
print(h.heappush(H,30))
print(h.heappush(H,40))

print(h.heappop(H))
print(h.heappop(H))

L = [50,30,60,40,20,10]
print(h.heapify(L))
print(L)
print(h.nlargest(2,L))
print(h.nsmallest(3,L))