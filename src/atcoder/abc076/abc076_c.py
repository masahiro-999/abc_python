ss, = input().split()
t, = input().split()

def cmp(a,b):
    for a1, b1 in zip(a,b):
        if a1 != b1 and a1 != "?":
            return False
    return True

size_t = len(t)
for i in range(len(ss)-size_t, -1, -1):
    if cmp(ss[i:i+size_t], t):
        ans = ss[:i] + t + ss[i+size_t:]
        ans = ans.replace('?', 'a')
        print(ans)
        exit()


print("UNRESTORABLE")

