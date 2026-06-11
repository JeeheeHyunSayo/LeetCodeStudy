'''
Q: 정렬된 배열에서 중복값 제거 및 남는 인자 수 반환
A:
    1. 초기 인덱스 0와 그 다음 값 비교
    2. 값이 같으면 pass 다르면 같은 값으로 변경 및 기준 인덱스 k+1 
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1
