from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def check(u):
    for k,x in u.all_group_members().items():
        c1 = 0
        c2 = 0
        c3 = 0
        if len(x) == 1:
            return False
        for y in x:
            if len(p[y]) == 1:
                c1 += 1
            elif len(p[y]) == 2:
                c2 += 1
            else:
                c3 += 1
        if c1 != 2 or c3 != 0:
            return False
    return True


N,M = map(int,input().split())

c = False
u = UnionFind(N)
p = {}
for i in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    x = p.get(a, [])
    x.append(a)
    p[a] = x
    x = p.get(b, [])
    x.append(b)
    p[b] = x
    u.union(a,b)

g = u.group_count()


if check(u):
    print("Yes")
else:
    print("No")
