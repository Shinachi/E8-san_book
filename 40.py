from matplotlib.font_manager import json_load


N = int(input())
A = list(map(int, input().split()))
C = [0]* (N-1)
C[0] = A[0]
for i in range(1, N-1):
    C[i] = C[i-1] + A[i]
M = int(input())
B = [int(input()) for i in range(M)]
C = [0] + C
ans = 0

for i in range(M-1):
    ans += abs(C[B[i]-1]-C[B[i+1]-1])
    
print(ans)

li = [1, 2,3,4,5,6,7,8,9,10]
di = {1,2,3,4,5,6,7,8,9,10}
x = set(1,2,3,4,5,6,7,8,9,10)

y = [2.4,6,67788]

cnt = 0
for i in y:
    for j in li:
        if i == j:
            cnt += 1
            
import collections
y = [2.4,6,67788]
c = collections.Counter(y)

for i in li:
    if i in 