N, K = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
a = list(set(a))

aa = a[:K]

if aa[0] != 0:
    print(0)
else:
    for i in range(len(aa)):
        if aa[i] != i:
            print(i)
            break
    else:
        print(K)
