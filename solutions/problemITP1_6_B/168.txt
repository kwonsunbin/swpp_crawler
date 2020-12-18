# coding: utf-8
card = [[0 for i in range(13)] for i in range(4)]
m=['S','H','C','D']

n=int(input())

for i in range(n):
    mark,num=(i for i in input().split())
    num=int(num)
    if mark=='S':
       card[0][num-1]=1
    elif mark=='H':
       card[1][num-1]=1
    elif mark=='C':
       card[2][num-1]=1
    elif mark=='D':
       card[3][num-1]=1

for i in range(4):
    for j in range(13):
        if card[i][j]==0:
            print("{} {}".format(m[i],j+1))
