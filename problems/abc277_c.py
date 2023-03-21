from collections import defaultdict, deque

N, = map(int,input().split())

t = defaultdict(list)

for i in range(N):
    a,b= map(int,input().split())
    t[a].append(b)
    t[b].append(a)

visited = set([1])
buf = deque()
buf.append(1)
while len(buf):
    n = buf.popleft()
    for i in t[n]:
        if not i in visited:
            buf.append(i)
            visited.add(i)
    
print(max(visited))