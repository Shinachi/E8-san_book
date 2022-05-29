import math

a, b, h, m = map(int, input().split())

PI = math.pi
H = 30* h + (1/2) *m
M = 6* m
hx = a* math.cos(H* PI/ 180)
hy = a* math.sin(H* PI/ 180)
mx = b* math.cos(M* PI/ 180)
my = b* math.sin(M* PI/ 180)

ans = math.sqrt((hx-mx)** 2 + (hy-my)** 2)
print(ans)