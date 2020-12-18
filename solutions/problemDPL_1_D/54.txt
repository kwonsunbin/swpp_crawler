# -*- coding: utf-8 -*-
"""
aaa
"""
#import re #正規表現
import sys
import bisect
#import heapq
#import collections
#import math

def main():
    length = int(input())
    X = [0] * length
    for i, line in enumerate(sys.stdin): 
        X[i] = int(line)
    print(LIS2(X))

def LIS(X):
    res = 0
    N = len(X)
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if i == 0: dp[0] = 1
            elif X[i] > X[j]: dp[i] = max(dp[i], dp[j]+1)
        res = max(res, dp[i])
    return res

def LIS2(X):
    INF = 10 ** 10
    N = len(X)
    dp = [INF] * (N+1)
    dp[0] = -1
    for a in X:
        idx = bisect.bisect_right(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)

    
if __name__ == '__main__':
    main()

