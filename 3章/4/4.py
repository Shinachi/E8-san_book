n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += (1//3)* a[i] + (2//3)* b[i]
    
print(ans)