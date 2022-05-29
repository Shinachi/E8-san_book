T = int(input())
N = int(input())
li = [0]* (T+2)
for i in range(N):
    L, R = map(int, input().split())
    li[L] += 1
    li[R] -= 1

li = [0] + li
for i in range(1, T+1):
    x = li[i-1] + li[i]
    li[i] = x
    if x < 0:
        print(0)
    else:
        print(x)