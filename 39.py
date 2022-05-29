N, Q = map(int, input().split())

li = [0]* (N+2)

for i in range(Q):
    L, R, X = map(int, input().split())
    li[L] += X
    li[R+1] -= X

ans = ''
for i in range(2, N+1):
    if li[i] > 0:
        ans += '<'
    elif li[i] == 0:
        ans += '='
    else:
        ans += '>'
        
print(ans)