N = int(input())
A = list(map(int, input().split()))
M = int(input())
S = [0]* (N+1)
for i in range(1, N):
    S[i] = S[i-1] + A[i-1]
B = []
for i in range(M):
    x = int(input())
    B.append(x)
    
ans = 0
for i in range(M-1):
    if B[i] > B[i+1]:
        ans += S[B[i]-1] - S[B[i+1]-1]
    else:
        ans += S[B[i+1]-1] - S[B[i]-1]
        
print(ans)