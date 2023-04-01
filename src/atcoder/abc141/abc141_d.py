import heapq

N,M = map(int, input().split())
a = list(map(int, input().split()))

a = [-i for i in a]
heapq.heapify(a)

for i in range(M):
    m = -heapq.heappop(a)
    heapq.heappush(a, -(m>>1))

print(-sum(a))