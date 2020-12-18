import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, W = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(N)]

    # i個目まで使って重さj以下の場合の最大価値
    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(0, W+1):
            v_i = vw[i-1][0]
            w_i = vw[i-1][1]
            if w_i<=j:
                dp[i][j] = max(dp[i-1][j-w_i]+v_i, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][W])

if __name__ == '__main__':
    resolve()
