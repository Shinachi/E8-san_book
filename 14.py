N = int(input())
ans_li = []
for i in range(2, int(N**0.5)+1):
    while N% i == 0:
        N //=i
        ans_li.append(i)

if N >= 2:
    ans_li.append(int(N))
    
print(*ans_li)