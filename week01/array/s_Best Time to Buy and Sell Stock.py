'''
    * 해결 방법 모든 상승분을 챙기면 최적해와 같아진다 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
        return profit