t = int(input())
n = int(input())
a = [0 for i in range(t+2)]
b = [0 for i in range(t+2)]
l = [0 for i in range(n)]
r = [0 for i in range(n)]
for i in range(n):
    l[i], r[i] = map(int, input().split())
    
for i in range(n):
    b[l[i]] += 1
    b[r[i]] -= 1
    
a[0] = b[0]
for i in range(1, t):
    a[i] = a[i-1] + b[i]
    
for i in range(t):
    print(a[i])