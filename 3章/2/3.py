def GCD(x, y, a, b):
    if x % y != 0:
        return GCD(y, x% y, a, b)
    else:
        return (a* b) / y
    
a = list(map(int, input().split()))
z = GCD(max(a[0], a[1]), min(a[0], a[1]), a[0], a[1])
for i in range(2, len(a)):
    z = GCD(z, a[i], z, a[i])
    
print(z)