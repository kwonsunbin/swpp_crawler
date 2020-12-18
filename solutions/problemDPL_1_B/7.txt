#!/usr/bin/env python3
import functools


def memorized(f):
    table = {}
    @functools.wraps(f)
    def wrapper(*args):
        if args in table:
            return table[args]
        rvalue = f(*args)
        table[args] = rvalue
        return rvalue
    return wrapper


N, W = map(int, input().split())
v, w = [], []
for _ in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

@memorized
def knapsack(i, r):
    if i == N:
        return 0
    if r < w[i]:
        return knapsack(i + 1, r)
    return max(knapsack(i + 1, r), v[i] + knapsack(i + 1, r - w[i]))

print(knapsack(0, W))

