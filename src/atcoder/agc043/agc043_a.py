H,W = map(int, input().split())

s = []
for i in range(H):
    s.append([x=="." for x in input()])

t = [[0]*W for i in range(H)]

if s[0][0]:
    t[0][0] = 0
else:
    t[0][0] = 1
    
for i in range(H):
    for j in range(W):
        if i==0 and j==0:
            continue
        if i != 0 and s[i-1][j] and (s[i][j]==False):
            di = 1
        else:
            di = 0
        if j != 0 and s[i][j-1] and (s[i][j]==False):
            dj = 1
        else:
            dj = 0

        if i == 0:
            t[i][j] = t[i][j-1] +dj
        elif j == 0:
            t[i][j] = t[i-1][j] +di
        else:
            t[i][j] = min(t[i-1][j]+di, t[i][j-1] +dj)

ans = t[H-1][W-1]
print(ans)
