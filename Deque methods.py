from collections import deque
L = [1,2,3,4,5]
q = deque(L)

print(q.append(6))
print(q.appendleft(7))
print(q.pop())
print(q.popleft())
print(q.extend([10,20,30]))
print(q.extendleft([11,22,33]))
print(q.rotate(2))
print(q)

print(q.count(5))
print(q.index(33))
print(q.insert(0,55))
print(q.reverse())