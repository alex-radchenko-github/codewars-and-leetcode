def maxProfit(prices):
    minn = []
    maxn = []
    for i in range(len(prices)-1):
        if prices[i] > prices[i+1]:
            continue
        else:
            minn.append(min(prices[i], prices[i+1]))
            maxn.append(max(prices[i], prices[i + 1]))
    if maxn == [] and minn == []:
        return 0
    else:
        return max(maxn) - min(minn), minn, maxn
print(maxProfit([7,1,5,3,6,4]))#5 - 1-6, [1-4]

#print(maxProfit([10, 7, 5, 8, 11, 9]))#6 [2-4]
#print(maxProfit([3, 4]))#1
#print(maxProfit([10, 7, 5, 4, 1]))#1
#print(maxProfit([7,6,4,3,1]))#
print(maxProfit([2,1,2,0,1]))#1