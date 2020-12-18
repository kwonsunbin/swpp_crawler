#!/usr/bin/env python3
# DPL_1_D: Combinatorial - Longest Increasing Subsequence


class SegmentTree:
    def __init__(self, n):
        size = 2**n.bit_length()
        self.size = 2*size - 1
        self.data = [0] * self.size

    def max(self, lo, hi):
        def _max(r, i, j):
            if j < lo or i > hi:
                return 0
            elif lo <= i and j <= hi:
                return self.data[r]
            else:
                mid = (i + j) // 2
                return max(_max(r*2+1, i, mid), _max(r*2+2, mid+1, j))

        return _max(0, 0, self.size//2)

    def set(self, i, v):
        r = self.size//2 + i
        self.data[r] = v
        while r > 0:
            r = (r-1) // 2
            self.data[r] = max(self.data[r*2 + 1], self.data[r*2 + 2])


def longest_increasing_subseq(vs):
    index = {v: i for i, v in enumerate(sorted(set(vs)))}
    seg = SegmentTree(len(index))
    c = 1

    for i in range(len(vs)):
        j = index[vs[i]]
        _c = seg.max(0, j-1)+1
        if _c > c:
            c = _c
        seg.set(j, _c)

    return c


def run():
    n = int(input())
    vs = []

    for _ in range(n):
        vs.append(int(input()))

    print(longest_increasing_subseq(vs))


if __name__ == '__main__':
    run()

