from collections import defaultdict

N,M = map(int,input().split())

def defaultvalue():
    return False
s=[]
t=defaultdict(defaultvalue)
for i in range(N):
    s.append(input())

for i in range(M):
    t[input()]=True

c = 0
for i in s:
    if t[i[-3:]]:
        c += 1

print(c)
