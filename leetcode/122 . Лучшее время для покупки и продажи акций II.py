def maxProfit(prices):
    rez = 0
    for i in range(len(prices)-1):
        if prices[i] > prices[i+1]:
            continue
        else:
            rez += (prices[i+1] - prices[i])
    return rez

print(maxProfit([7,1,5,3,6,4]))#5 - 1-6, [1-4]

#print(maxProfit([10, 7, 5, 8, 11, 9]))#6 [2-4]
#print(maxProfit([3, 4]))#1
#print(maxProfit([10, 7, 5, 4, 1]))#1
#print(maxProfit([7,6,4,3,1]))#1
#print(maxProfit([2,4,1]))#1