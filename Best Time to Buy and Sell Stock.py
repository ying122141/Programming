class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = 0
        
        for p in prices:
            if p < minPrice:
                minPrice = p
            
            diff = p - minPrice
            
            if diff > profit:
                profit = diff
        
        return profit