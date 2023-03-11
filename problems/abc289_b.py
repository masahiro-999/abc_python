N, M = map(int,input().split())
a = list(map(int,input().split()))

c = {}

for i in a:
    c[i-1] = True

r = []
s = []
for i in range(N):
    if c.get(i, False) :
        s.append(i+1)
    else:
        r.append(i+1)
        s.reverse()
        r.extend(s)
        s = []
r.extend(s)

print(*r)
