
def maxProfit(prices) :
        
        maxProfit = 0
        minprice = float('inf')
        
        for i in range(len(prices)):
            if(prices[i] < minprice):
                minprice = prices[i]
            elif(prices[i] - minprice > maxProfit):
                maxProfit = prices[i] - minprice
        return maxProfit

print(maxProfit([7,1,5,3,6,4]))