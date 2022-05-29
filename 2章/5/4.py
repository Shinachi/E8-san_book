def isprime(x):
    for i in range(2, x):
        if i % x == 0:
            return False
        
    return True
            
    

n = int(input())
li = []
for i in range(2, n+1):
    if isprime(i):
        li.append(i)
        
print(*li)