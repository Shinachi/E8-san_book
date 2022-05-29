n = int(input())
a = list(map(int, input().split()))
dp1 = [0] * (n+1)
dp2 = [0] * (n+1)
dp1[0], dp2[0] = 0, 0
for i in range(1,n+1):
    dp1[i] = dp2[i-1] + a[i-1]
    dp2[i] = max(dp1[i-1], dp2[i-1])
    
print(max(dp1[n], dp2[n]))