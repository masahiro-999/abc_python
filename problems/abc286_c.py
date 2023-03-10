N,A,B = map(int,input().split())
s = input()
l = N

def count_diff(s,start,l):
    count = 0
    for i in range(l//2):
        if s[start+i] != s[start+l-i-1]:
            count += 1
    return count

result = B*count_diff(s,0,l)

max_na = result // A
ss = s+s
for i in range(l-1):
    result = min(result, A * (i+1) + B * count_diff(ss, i+1, l))

print(result)