'''
Q: 두 배열의 공통 배열 찾기
A:
    1. 길이가 더 짧은 배열로 해시테이블 생성 (각 숫자가 몇개씩 있는지 확인)
    2. 두 번째 배열 숫자가 해시테이블에 존재하는 만큼 res에 추가
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        # Hash Table
        cnt = {}
        for i in nums1:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
                
        res = []
        for num in nums2:
            if num in cnt and cnt[num] > 0:
                res.append(num)
                cnt[num] -= 1
        return res