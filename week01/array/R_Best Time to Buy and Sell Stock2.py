'''
Q: 배열 값 비교하여 최대이윤 찾기
A:
    인덱스 i와 i+1 값을 비교하여 i+1의 값이 더 큰 경우 profit+ 
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit