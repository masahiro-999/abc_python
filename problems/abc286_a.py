N, P,Q,R,S = map(int,input().split())

P -= 1
Q -= 1
R -= 1
S -= 1
a = list(map(int,input().split()))
a[R:S+1],a[P:Q+1] = a[P:Q+1],a[R:S+1]
print(*a)