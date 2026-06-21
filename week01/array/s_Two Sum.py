class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            number = target - n 
            if number in num_dict:
                return[num_dict[number], i]
            num_dict[n] = i 
            