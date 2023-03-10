N, = map(int,input().split())
c = 0
for i in range(N):
    s= input()
    if s == "For":
        c += 1
if N//2 < c:
    print("Yes")
else:
    print("No")
