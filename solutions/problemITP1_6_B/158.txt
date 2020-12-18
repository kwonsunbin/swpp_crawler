lst = [True for i in range(52)]
n = int(input())
for i in range (n):
    suit, rank = input().split()
    rankn = int(rank)
    if suit == 'S':
        lst[rankn-1] = False
    elif suit == 'H':
        lst[rankn+12] = False
    elif suit == 'C':
        lst[rankn+25] = False
    else:
        lst[rankn+38] = False
for i in range(52):
    tf = lst[i]
    if i <= 12 and tf:
        print ('S %d' % (i+1))
    elif 12 < i <= 25 and tf:
        print ('H %d' % (i-12))
    elif 25 < i <= 38 and tf:
        print ('C %d' % (i-25))
    elif tf:
        print ('D %d' % (i-38))
