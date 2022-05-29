import queue


R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
c = [input() for i in range(R)]
start = (sx-1)* C + (sy-1)
goal = (gx -1)* C + (gy-1)

G = [[] for i in range(R* C)]
for i in range(R):
    for j in range(C-1):
        if c[i][j] == '.' and c[i][j+1] == '.':
            idx1 = i* C + j
            idx2 = i* C + (j+1)
            G[idx1].append(idx2)
            G[idx2].append(idx1)
            
for i in range(R-1):
    for j in range(C):
        if c[i][j] == '.' and c[i+1][j] == '.':
            idx1 = i* C + j
            idx2 = (i+1)* C + j
            G[idx1].append(idx2)
            G[idx2].append(idx1)
            
dist = [-1]* (R* C)
Q = queue.Queue()
dist[start] = 0
Q.put(start)

while not Q.empty():
    pos = Q.get()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.put(nex)
            
print(dist[goal])