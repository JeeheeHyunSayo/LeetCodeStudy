from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums2) 
        result = []
        for num in nums1:
            if counter[num] > 0:
                result.append(num)
                counter[num] -= 1 
        return result