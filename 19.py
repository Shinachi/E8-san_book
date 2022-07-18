from collections import Counter
def main():
    N = int(input())
    A = Counter(list(map(int, input().split())))
    A = A.items()

    ans = 0
    for i in A:
        ans += (i[1]*(i[1]-1))// 2
        
    print(ans)

if __name__=='__main__':
    main()