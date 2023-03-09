n, = map(int,input().split())
s = input()

for i in range(1,n):
    for k in range(n-i):
        if s[k] == s[k+i]:
            k -= 1
            break
    print(k+1) 

