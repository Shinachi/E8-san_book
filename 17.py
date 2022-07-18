import math

N = int(input())
A = list(map(int, input().split()))
x = math.gcd(A[0], A[1])
ans = (A[0]* A[1])// x

for i in range(2, N):
    x = math.gcd(ans, A[i])
    ans = (ans* A[i])// x
    
print(ans)