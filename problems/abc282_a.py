k, = map(int,input().split())

s=""
for i in range(k):
    s += chr(ord("A")+i)

print(s)