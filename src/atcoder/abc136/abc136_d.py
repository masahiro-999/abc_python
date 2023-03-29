# RRLRL
s = input()
# d[0][i] 1回移動した時iの移動先
d = [[0]*len(s) for i in range(30)]


for i,k in enumerate(s):
    if k == "R":
        d[0][i] = i+1
    elif k =="L":
        d[0][i] = i-1

for p in range(29):
    for i in range(len(s)):
        d[p+1][i] = d[p][d[p][i]]


ans = [0]*len(s)
for i in range(len(s)):
    ans[d[29][i]] += 1

print(*ans)
