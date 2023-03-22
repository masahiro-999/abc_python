s = input()
t = input()

for i,a,b in zip(range(len(s)),s,t):
    if a!=b:
        print(i+1)
        exit()
print(len(t))

