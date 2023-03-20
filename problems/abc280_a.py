H, W= map(int,input().split())

ans = 0
for i in range(H):
    s = input()
    for i in s:
        if i == "#":
            ans += 1
print(ans)