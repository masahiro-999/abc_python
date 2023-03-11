N, M = map(int,input().split())

c=[]
for i in range(M):
    cn = input()
    a = list(map(int,input().split()))
    v = 0
    for j in a:
        v += 1<<(j-1)
    c.append(v)

count = 0
for i in range(1,(1<<M)):
    x = 0
    for j in range(M):
        if i & 1 == 1:
            x = x | c[j]
        i = i >> 1
    if x == (1 << N) -1:
        count += 1
print(count)
