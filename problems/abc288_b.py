N, K = map(int,input().split())

l = []
for i in range(K):
    l.append(input())

l.sort()

for x in l:
    print(x)