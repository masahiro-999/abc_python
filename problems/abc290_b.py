N, K = map(int,input().split())
s = input()

out = ""
count = 0
for i in range(N):
    if s[i] == "o":
        count += 1
        if count >= K:
            break

out = s[:i+1] + "x" * (N -i-1)
print(out)