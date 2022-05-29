import math
def func(a, b):
    ans = math.sqrt((a[0]-b[0])** 2 + (a[1]-b[1])** 2)
    return ans

n = int(input())
li = []
for i in range(n):
    s = list(map(int, input().split()))
    li.append(s)
    
ans = 10000000000
for i in range(n):
    for j in range(i+1, n):
        y = func(li[i], li[j])
        ans = min(ans, y)
        
print(ans)