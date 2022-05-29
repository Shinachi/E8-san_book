N, M = map(int, input().split())
G = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(1, N+1):
    G[i].sort()
    if len(G[i]) > 1:
        if G[i][0] < i and G[i][1] >= i:
            ans += 1
    else:
        if G[i][0] < i:
            ans += 1
        
print(ans)