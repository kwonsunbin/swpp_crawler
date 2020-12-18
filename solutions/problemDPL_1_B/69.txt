from typing import Callable


class DynamicProgramming(object):

    table: list
    obj_coef: list
    sbj_coef: list

    def __init__(self, item_n: int, border: int):
        self.item_n = item_n
        self.border = border

    def __str__(self):
        return "\n".join(list(map(lambda l:
                                  " ".join(list(map(str, l)))
                                  , self.table)))

    def __repr__(self):
        return "DynamicProgramming object:\n" + \
               "item_n: " + str(self.item_n) + ", border: " + str(self.border) + "\n" +\
               "table:\n" + self.__str__()

    def solve(self, obj_coef: list, sbj_coef: list, expr: Callable[[int, int], int], initializer=0) -> list:
        self.table = [[initializer for _ in range(self.item_n + 1)] for _ in range(self.border + 1)]

        if len(obj_coef) == self.item_n:  # to 1-base
            obj_coef = [None] + obj_coef
        self.obj_coef = obj_coef

        if len(sbj_coef) == self.item_n:
            sbj_coef = [None] + sbj_coef
        self.sbj_coef = sbj_coef

        for weight_lim in range(1, self.border + 1):
            for item_idx in range(1, self.item_n + 1):
                self.table[weight_lim][item_idx] = expr(weight_lim, item_idx)

        return self.table

    def knapsack_expr(self, weight_lim: int, item_idx: int) -> int:
        res = self.table[weight_lim][item_idx - 1]
        if weight_lim - self.sbj_coef[item_idx] >= 0:
            res = max(res, self.table[weight_lim - self.sbj_coef[item_idx]][item_idx - 1] + self.obj_coef[item_idx])
        return res


if __name__ == '__main__':
    N, W = map(int, input().split())
    v, w = [], []
    for i in range(N):
        buff = [int(j) for j in input().split()]
        v.append(buff[0])
        w.append(buff[1])

    dp = DynamicProgramming(N, W)
    print(dp.solve(v, w, dp.knapsack_expr)[W][N])

