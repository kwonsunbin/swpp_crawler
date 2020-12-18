from bisect import bisect_left


def main():
    n = int(input())
    a = [-1] * n
    for i in range(n):
        a[i] = int(input())

    ans = solve3(n, a)
    # print("ans={}".format(ans))
    print(ans)


def solve1(n, a):
    INF = 10 ** 9
    dp = [INF for i in range(n + 1)]
    for i in range(n):
        for j in range(1, i + 2):
            if j == 1 or a[i] > dp[j - 1]:
                dp[j] = min(dp[j], a[i])

    ret = 0
    for i in range(n + 1):
        if dp[i] < INF:
            ret = i
    return ret


def solve2(n, a):
    INF = 10 ** 9
    dp = [INF for i in range(n)]
    for i in range(n):
        for j in range(i + 2):
            if j == 0 or a[i] > dp[j - 1]:
                dp[j] = min(dp[j], a[i])
    ans = 0
    for i in range(n):
        if dp[i] < INF:
            ans = i + 1
    return ans


def solve3(n, a):
    INF = 10 ** 9
    dp = [INF for i in range(n)]
    for i in range(n):
        ix = bisect_left(dp, a[i])
        dp[ix] = a[i]
    ans = bisect_left(dp, INF)
    return ans


def solve4(n, a):
    INF = 10 ** 10
    dp = [INF for i in range(n)]
    for elt in a:
        ix = bisect_left(dp, elt)
        dp[ix] = elt

    ans = 0
    for i in range(n):
        if dp[i] < INF:
            ans = i + 1

    return ans


main()

