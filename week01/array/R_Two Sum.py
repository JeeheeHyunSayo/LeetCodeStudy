'''
Q: 배열에서 합이 target이 되는 두 수의 indices를 반환 
A:
    O(n^2) time complexity
    1. 인덱스 i와 i+1~의 합을 계산
    2. 합이 target과 일치하면 반복 for문 탈출
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    flag = True
                    break
            if flag:
                break
        return [i,j]
