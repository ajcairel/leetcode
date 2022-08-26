class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right 
            right += 1
            
        return max_profit
    
    
    # if left is more than right, then left becomes right 
    # Input = [7,2,5,3,6,4,1,7]
    # Output = 6 (7 - 1)
    # 2 was the lowest until it hit 1 
            
        