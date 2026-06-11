'''
Q: 리스트 회전 시키기
A:
    (슬라이싱으로 시도했는데 안됨)
    1. 회전수 k를 배열의 길이로 나눈 나머지로 변경
    1-1. 나머지가 0인 경우: 회전시킨 결과가 처음 배열과 동일
    1-2. 나머지가 0이 아닌 경우: 나머지만큼 회전
    2. 배열을 확장시킨 후, 중복되는 부분 제거
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k%l:
            k = k%l
            # nums = nums[-k:] + nums[:-k]
            nums.extend(nums[:-k])
            del nums[:l-k]