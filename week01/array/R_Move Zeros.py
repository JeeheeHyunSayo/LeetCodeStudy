'''
Q: 배열값 중 0만 뒤로 옮기기
A:
    1. 배열값이 0이면 0 개수 카운트(zeros ++)
    2. 값이 0이 아니면
        2-1. 0이 앞에 존재한 경우 마지막 위치로 이동(last)
        2-2. 0이 없었던 경우 위치값만 증가(last ++)
    3. zeros 값만큼 배열 뒤의 값들을 0으로 변경
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        last = 0
        for i, v in enumerate(nums):
            if v == 0:
                zeros += 1
            else:
                if zeros > 0:
                    nums[last] = v
                last += 1
        for i in range(zeros):
            nums[-i-1] = 0