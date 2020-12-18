n, W = input().split()
n = int(n)
W = int(W)

items = []
for _ in range(n):
    v, w = input().split()
    items.append((int(v), int(w)))

dp = [[0 for _ in range(n+1)] for _ in range(W+1)]

for i in range(1, W+1):
     for j in range(1, n+1):
         value = items[j-1][0]
         weight = items[j-1][1]
         if i >= weight:
             dp[i][j] = max(dp[i][j-1], dp[i-weight][j-1]+value)
         else:
             dp[i][j] = dp[i][j-1]

print(dp[W][n])
