N, M = map(int,input().split())

s=[]
for i in range(N):
    str = input()
    b = 0
    for i in str:
        b <<= 1
        if i =="o":
            b += 1
    s.append(b)

ok = 0
for i in range(N):
    for j in range(N):
        if i==j or j>i:
            continue
        if s[i] | s[j] == (1<<M)-1:
            ok += 1

print(ok)