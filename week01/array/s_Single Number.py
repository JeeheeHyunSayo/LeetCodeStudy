from collections import Counter 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = [num for num, cnt in counter.items() if cnt == 1 ]
        return result[0]
        