import sys

def dfs(pos, G, color):
    for i in G[pos]:
        if color[i] == 0:
            color[i] = 3-color[pos]
            dfs(i, G, color)

sys.setrecursionlimit(120000)

N, M = map(int, input().split())
A = [None]* M
B = [None]* M

for i in range(M):
    A[i], B[i] = map(int, input().split())
    
G = [[] for i in range(N+1)]

for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])
    
color = [0]* (N+1)

for i in range(1, N+1):
    if color[i] == 0:
        color[i] = 1
        dfs(i, G, color)
        
ans = True
for i in range(M):
    if color[A[i]] == color[B[i]]:
        ans = False
        
if ans:
    print('Yes')
else:
    print('No')