while True:
    n, x = map(int, input().split())

    ans=0
    if n == 0 and x == 0:
        break
    for n1 in range(1,n-1):
        for n2 in range(n1+1,n):
            n3=x-n1-n2
            if n2<n3<=n:
                ans+=1
    print(ans)
