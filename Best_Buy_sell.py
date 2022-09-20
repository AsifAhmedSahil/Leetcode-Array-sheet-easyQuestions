
def maxProfit(self, prices: list[int]) -> int:
        
        maxProfit = 0
        minprice = 0
        
        for i in range(len(prices)):
            if(prices[i] < minprice):
                minprice = prices[i]
            elif(prices[i] - minprice > maxProfit):
                maxProfit = prices[i] - minprice
        return maxProfit

print(maxProfit([7,1,5,3,6,4]))