import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

class Segtree: #1-indexed
    def __init__(self, n, A, segfunc, ide_ele):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        #　配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = A[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
        
    def update(self, ind, val): #0-indexed
        ind += self.num
        self.tree[ind] = val
        while ind > 1:
            self.tree[ind >> 1] = self.segfunc(self.tree[ind], self.tree[ind^1])
            ind >>= 1

    def find(self, l, r): #[1, r), 0-indexed
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N = ii()
A = [ii() for i in range(N)]
compress = lambda arr: list(map({e: i for i, e in enumerate(sorted(set(arr)))}.__getitem__, arr))
A = compress(A)
'''
# 座標圧縮
d = defaultdict(int)
for i, num in enumerate(sorted(list(set(A)))):
    d[num] = i
for i, num in enumerate(A):
    A[i] = d[num]
'''
# Segtreeを用いたDP
dp = [0 for _ in range(N)]
seg = Segtree(N, dp, max, 0)

for num in A:
    dp[num] = seg.find(0, num) + 1
    seg.update(num, dp[num])

print(max(dp))
    
