N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0]* N

B[0] = A[0]

for i in range(1, N):
    B[i] = B[i-1] + A[i]
   
B = [0] + B 
for i in range(Q):
    L, R = map(int, input().split())
    print(B[R]-B[L-1])