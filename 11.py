def main():
    N = int(input())
    ans = []
    for i in range(2, N+1):
        cnt = 0
        for j in range(1, i):
            if j == 1:
                continue
            if i% j == 0:
                cnt += 1
        if cnt == 0:
            ans.append(i)
        
    for i in ans:
        print(i)
    
if __name__=='__main__':
    main()