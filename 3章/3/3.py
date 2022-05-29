n, r = map(int, input().split())
x = n - r
cnt1 = 1
cnt2= 1
for i in range(x+1, n):
    cnt1 *= i
for i in range(1, x):
    cnt2 *= i
    
print(cnt1/cnt2)